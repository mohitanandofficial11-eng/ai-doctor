import re
import random
import os
import base64
from .knowledge_base import (SYMPTOMS_DB, SPECIALTIES, SURGERY_INFO,
                              MEDICINES_DB, DOCTOR_PROFILE, GREETINGS,
                              EMERGENCY_KEYWORDS)
from .hinglish import HinglishProcessor
from .prescription_gen import PrescriptionGenerator

# Groq integration (free, fast Llama 3 models)
AI_AVAILABLE = False
AI_CLIENT = None
AI_MODEL = "llama-3.3-70b-versatile"
AI_VISION_MODEL = "llama-3.2-11b-vision-preview"
try:
    from groq import Groq
    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        key_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "groq_key.txt")
        if os.path.exists(key_file):
            with open(key_file) as f:
                api_key = f.read().strip()
    if not api_key:
        import streamlit as st
        api_key = st.secrets.get("GROQ_API_KEY", "")
    if api_key:
        AI_CLIENT = Groq(api_key=api_key)
        AI_AVAILABLE = True
except Exception:
    pass


FOLLOW_UP_QUESTIONS = {
    "fever": {
        "en": ["Since how many days do you have fever?", "What is the temperature?", "Any other symptoms like cough or body ache?"],
        "hi": ["बुखार को कितने दिन हो गए?", "तापमान कितना है?", "खांसी या बदन दर्द जैसे और लक्षण हैं?"]
    },
    "headache": {
        "en": ["Since when is the headache?", "Is it mild or severe?", "Any other symptoms like nausea or eye strain?"],
        "hi": ["सिरदर्द कब से है?", "हल्का है या तेज?", "मतली या आंखों में जलन जैसे और लक्षण हैं?"]
    },
    "chest_pain": {
        "en": ["Is the pain constant or coming and going?", "Any difficulty breathing?", "Do you feel it on left or right side?"],
        "hi": ["दर्द लगातार है या आता-जाता है?", "सांस लेने में तकलीफ है?", "बाएं या दाएं तरफ दर्द है?"]
    },
    "acidity": {
        "en": ["After eating or empty stomach?", "Do you feel burning in chest?", "Any sour taste in mouth?"],
        "hi": ["खाने के बाद या खाली पेट?", "सीने में जलन होती है?", "मुंह में खट्टा स्वाद आता है?"]
    },
    "back_pain": {
        "en": ["Since when is the back pain?", "Did you lift something heavy?", "Pain going down to legs?"],
        "hi": ["पीठ दर्द कब से है?", "क्या भारी चीज उठाई थी?", "दर्द पैरों में जाता है?"]
    },
    "skin_rash": {
        "en": ["Since when is the rash?", "Is there itching?", "Any new food or medicine?"],
        "hi": ["दाने कब से हैं?", "खुजली है?", "कोई नया खाना या दवा ली है?"]
    },
    "cough_cold": {
        "en": ["Dry cough or with phlegm?", "Running nose?", "Any fever?"],
        "hi": ["सूखी खांसी या बलगम वाली?", "नाक बह रही है?", "बुखार है?"]
    },
    "diarrhea": {
        "en": ["Since how many days?", "Blood in stool?", "Any vomiting?"],
        "hi": ["कितने दिनों से है?", "मल में खून है?", "उल्टी हो रही है?"]
    },
    "high_bp": {
        "en": ["What is your BP reading?", "Are you on any medicine?", "Any headache or dizziness?"],
        "hi": ["BP की रीडिंग क्या है?", "कोई दवा ले रहे हैं?", "सिरदर्द या चक्कर है?"]
    },
    "appendicitis": {
        "en": ["Pain in right lower side?", "Any fever or vomiting?", "Appetite loss?"],
        "hi": ["दाहिनी निचली तरफ दर्द है?", "बुखार या उल्टी है?", "भूख नहीं लग रही?"]
    },
    "kidney_stone": {
        "en": ["Pain in back or side?", "Blood in urine?", "Pain while passing urine?"],
        "hi": ["पीठ या बाजू में दर्द?", "पेशाब में खून?", "पेशाब करने में दर्द?"]
    },
    "diabetes": {
        "en": ["Fasting or random sugar level?", "Any medicine already?", "Excessive thirst or urination?"],
        "hi": ["खाली पेट या खाने के बाद शुगर?", "पहले से कोई दवा?", "बहुत प्यास लगना या पेशाब आना?"]
    },
    "depression": {
        "en": ["Since how long are you feeling this way?", "Sleep and appetite changes?", "Any thoughts of self-harm?"],
        "hi": ["कितने समय से ऐसा महसूस कर रहे हैं?", "नींद और भूख में बदलाव?", "खुद को नुकसान पहुंचाने के विचार?"]
    },
    "anxiety": {
        "en": ["Since when are you feeling anxious?", "What triggers your anxiety? (work, social, health)",
               "Any physical symptoms like racing heart, sweating?"],
        "hi": ["कब से चिंता महसूस कर रहे हैं?", "क्या चीज़ आपकी चिंता बढ़ाती है? (काम, सामाजिक, स्वास्थ्य)",
               "कोई शारीरिक लक्षण जैसे तेज़ दिल की धड़कन, पसीना?"]
    }
}


class MedicalDoctorAI:
    def __init__(self):
        self.hinglish = HinglishProcessor()
        self.conversation_history = []
        self.patient_info = {"name": "", "age": "", "gender": "", "weight": ""}
        self.current_symptoms = []
        self.reported_symptoms = []
        self.stage = "ask_name"
        self.follow_up_asked = set()
        self.follow_up_count = 0
        self.greeted = False
        self.use_ai = AI_AVAILABLE
        self.last_ai_advice = ""  # Stores the last AI advice text for PDF use

    def detect_danger(self, text):
        text_lower = text.lower()
        emergency_words = EMERGENCY_KEYWORDS.get(
            self.hinglish.detect_language(text), EMERGENCY_KEYWORDS["en"])
        for word in emergency_words:
            if word in text_lower:
                return True
        red_flag_patterns = [
            r"(can't|not|no)\s*(breathe|breathing)",
            r"(unconscious|passed out|faint|fainted)",
            r"(severe|very bad|unbearable|extreme)\s*(pain|bleeding)",
            r"(blood|khoon|rakat)\s*(vomit|cough|stool|urine|piss)",
            r"chest\s*pain",
            r"(heart|dil)\s*(attack|pain)",
            r"(paralysis|paralyz)",
            r"suicide|kill myself|want to die|end my life",
            r"(head|brain)\s*(injury|trauma|hurt|bleed)",
            r"gunshot|stabbing|knife",
            r"(burn|fire)\s*(severe|bad|3rd|third)",
            r"allergic\s*reaction\s*(severe|bad|swelling|breathing)",
            r"snake\s*bite|scorpion\s*sting",
            r"(drowning|choking|suffocat)",
        ]
        for p in red_flag_patterns:
            if re.search(p, text_lower):
                return True
        return False

    def _is_symptom_word(self, word):
        """Check if a word looks like a symptom rather than a name."""
        word_lower = word.lower().strip()
        # Common symptom-like patterns
        symptom_indicators = [
            "pain", "dard", "fever", "bukhar", "cough", "khansi", "cold",
            "headache", "headeach", "migraine", "sardard", "sir", "chest",
            "acidity", "gas", "back", "kamar", "rash", "skin", "itching",
            "diarrhea", "dast", "vomit", "ulti", "nausea", "infection",
            "stone", "sugar", "diabetes", "bp", "pressure", "depression",
            "anxiety", "tension", "stress", "fatigue", "thakaan", "insomnia",
            "neend", "allergy", "hives", "constipation", "kabj", "joint",
            "arthritis", "eye", "aankh", "ear", "kaan", "period", "cramps",
            "injury", "hit", "hurt", "cut", "wound", "bleed", "khoon",
            "swell", "sujan", "burn", "jala", "fracture", "hair",
        ]
        return word_lower in symptom_indicators

    def extract_patient_info(self, text):
        text_lower = text.lower()
        patterns = {
            "age": [
                r"(\d+)\s*(year|yr|saal|sal)\s*(old|ka|ki|puran|purana)",
                r"age\s*(is|:)?\s*(\d+)",
                r"(\d+)\s*(saal|sal|years|year)",
                r"(meri|mera|my)\s*(age|umar|umr)\s*(\d+)",
                r"(\d+)\s*(year|saal|sal)\s*(old|ka|ki)",
                r"(\d+)\s*(?:yo|yr)",
            ],
            "name": [
                r"(my name is|i'm|i am|mera naam|mera nam)\s*(\w+)",
                r"name\s*(is|:)?\s*(\w+)",
                r"call me\s*(\w+)",
                r"i am\s*(\w+)",
            ],
            "gender": [
                r"\b(male|female|man|woman|mard|aurat|ladka|ladki|boy|girl)\b",
            ]
        }
        for key, pats in patterns.items():
            for p in pats:
                m = re.search(p, text_lower, re.IGNORECASE)
                if m:
                    groups = m.groups()
                    for g in groups:
                        if g and g.strip():
                            self.patient_info[key] = groups[-1].strip()
                            break
                    break

    def extract_symptoms(self, text):
        found = []
        text_lower = text.lower()
        # Detect negation patterns: "not X", "no X", "nahi X", "sorry X", "galati X"
        negated = set()
        neg_pattern = r"(not\s+|no\s+|nahi\s+|nhi\s+|sorry\s+|galati\s+|galat\s+)("
        terms = []
        for sym_id, sym_data in SYMPTOMS_DB.items():
            for keyword in sym_data["en"]:
                terms.append(keyword)
        neg_re = neg_pattern + "|".join(re.escape(t) for t in terms) + r")"
        for m in re.finditer(neg_re, text_lower):
            for sym_id, sym_data in SYMPTOMS_DB.items():
                if m.group(2) in sym_data["en"]:
                    negated.add(sym_id)
        for sym_id, sym_data in SYMPTOMS_DB.items():
            for keyword in sym_data["en"]:
                if keyword in text_lower and sym_id not in negated:
                    if sym_id not in found:
                        found.append(sym_id)
                    break
        for sym_id, sym_data in SYMPTOMS_DB.items():
            if sym_id not in found and sym_id not in negated:
                hi_keywords = [k for k in sym_data.get("keywords", []) if any(
                    ord(c) >= 0x0900 for c in k)]
                for kw in hi_keywords:
                    if kw in text_lower:
                        found.append(sym_id)
                        break
        self.current_symptoms = found
        return found

    def identify_specialty(self, symptoms):
        specialty_scores = {}
        for sym_id in symptoms:
            if sym_id in SYMPTOMS_DB:
                sym_data = SYMPTOMS_DB[sym_id]
                for spec_id, spec_data in SPECIALTIES.items():
                    score = 0
                    for kw in sym_data["en"]:
                        if kw in " ".join(spec_data["keywords"]):
                            score += 1
                    if score > 0:
                        specialty_scores[spec_id] = specialty_scores.get(spec_id, 0) + score
        if not specialty_scores:
            return "general"
        return max(specialty_scores, key=specialty_scores.get)

    def _is_prescription_request(self, text):
        lower = text.lower().strip()
        keywords = [
            "prescription", "prescription do", "prescription de", "prescription dijiye",
            "prescribe", "prescribe do", "prescribe de", "prescribe dijiye",
            "parcha", "parcha do", "parcha likh", "parcha de", "parcha dijiye",
            "give me prescription", "give me prescribe",
            "prescription den", "prescription dedo",
            "rx", "nuskha", "nuskha likh", "nuskha do",
            "medicine likh", "dawai likh", "dawai do", "medicine do",
            "come to the point", "point pe aao", "sahi se batao",
            "shortcut", "short me batao",
            "prescription pdf", "pdf prescription", "pdf do", "pdf de",
            "download prescription", "prescription download",
            "priscription", "priscription do",
        ]
        return any(kw in lower for kw in keywords)

    def _ask_name(self, lang):
        if lang == "hi":
            return "Namaste! 🏥 Main Dr. Aarogya hoon. Aapka naam kya hai?"
        return "Namaste! 🏥 I'm Dr. Aarogya. What's your name?"

    def _ask_age(self, lang):
        name = self.patient_info.get("name", "")
        prefix = f"{name} ji, " if name else ""
        if lang == "hi":
            return f"{prefix}Aapki umar kya hai? (kitne saal)"
        return f"{prefix}What is your age?"

    def _ask_concern(self, lang):
        name = self.patient_info.get("name", "")
        prefix = f"{name} ji, " if name else ""
        if lang == "hi":
            return f"{prefix}Dhanyavaad! Ab mujhe batao ki aapko kya problem hai? Kya takleef hai?"
        return f"{prefix}Thank you! Now tell me, what health concern are you facing?"

    def process_message_with_attachment(self, text_message, files):
        """Process message with attached files (images, PDFs)."""
        lang = self.hinglish.detect_language(text_message) if text_message else "en"
        self.extract_patient_info(text_message)

        text_context = ""
        vision_images = []

        for f in files:
            ftype = f["type"]; fbytes = f["bytes"]; fname = f["name"]
            if ftype and ftype.startswith("image"):
                b64 = base64.b64encode(fbytes).decode("utf-8")
                mime = ftype if ftype else "image/jpeg"
                vision_images.append({"mime": mime, "b64": b64, "name": fname})
            elif ftype == "application/pdf":
                try:
                    import fitz
                    doc = fitz.open(stream=fbytes, filetype="pdf")
                    pdf_text = "".join(page.get_text() for page in doc)
                    doc.close()
                    if pdf_text.strip():
                        text_context += f"\n--- {fname} ---\n{pdf_text.strip()[:3000]}\n"
                except:
                    text_context += f"\n--- {fname} ---\n[Could not extract text]\n"
            elif ftype and ftype.startswith("video"):
                text_context += f"\n--- {fname} ---\n[Video file: {fname}]\n"

        full_msg = text_message if text_message else "Please analyze this file"
        if text_context:
            full_msg += "\n\nAttached file content:\n" + text_context
        if vision_images:
            full_msg += f"\n\n[{len(vision_images)} image(s) attached]"

        self.conversation_history.append({
            "role": "user", "message": full_msg, "lang": lang,
            "files": [f["name"] for f in files]
        })
        return self._ai_respond_with_files(full_msg, lang, vision_images)

    def _ai_respond_with_files(self, user_message, lang, vision_images=None):
        try:
            context = self._build_patient_context()
            sys_prompt = (
                "You are Dr. Aarogya, an AI medical assistant. Talk like a real experienced doctor - "
                "warm, empathetic, and professional.\n\n"
                f"Patient Context:\n{context}\n\n"
                "Guidelines:\n- Analyze any attached files (medical reports, images, etc.)\n"
                "- If analyzing an image (X-ray, MRI, ultrasound, wound photo), describe what you see\n"
                "- For lab reports/PDFs, interpret the values and flag abnormalities\n"
                "- Give concise, helpful medical insights\n"
                "- Always include disclaimer: 'This is AI analysis - consult a doctor'\n"
                f"Respond in {'Hinglish' if lang == 'hi' else 'English'} naturally."
            )
            if vision_images:
                content = [{"type": "text", "text": user_message}]
                for img in vision_images:
                    content.append({"type": "image_url", "image_url": {"url": f"data:{img['mime']};base64,{img['b64']}"}})
                messages = [{"role": "system", "content": sys_prompt}, {"role": "user", "content": content}]
                response = AI_CLIENT.chat.completions.create(
                    model=AI_VISION_MODEL, messages=messages, max_tokens=1000, temperature=0.7
                )
            else:
                messages = [{"role": "system", "content": sys_prompt}]
                for m in self.conversation_history[-10:]:
                    messages.append({"role": "user" if m["role"] == "user" else "assistant", "content": m["message"]})
                messages.append({"role": "user", "content": user_message})
                response = AI_CLIENT.chat.completions.create(
                    model=AI_MODEL, messages=messages, max_tokens=800, temperature=0.7
                )
            text = response.choices[0].message.content.strip()
            self.conversation_history.append({"role": "assistant", "message": text, "lang": lang})
            return {"response": text, "lang": lang, "role": "doctor"}
        except Exception as e:
            return self._fallback_response(lang)

    def process_message(self, user_message):
        lang = self.hinglish.detect_language(user_message)

        self.extract_patient_info(user_message)
        self.conversation_history.append({"role": "user", "message": user_message, "lang": lang})

        # Stage 1: Ask for name
        if self.stage == "ask_name":
            if not self.patient_info.get("name"):
                # If patterns didn't catch it, take entire clean input as name
                clean = user_message.strip().title()
                # Don't treat symptom words as names
                if clean and len(clean.split()) <= 3 and not self._is_symptom_word(clean):
                    self.patient_info["name"] = clean
            if self.patient_info.get("name"):
                self.stage = "ask_age"
                if self.patient_info.get("age"):
                    self.stage = "consult"
                    return {"role": "doctor", "response": self._ask_concern(lang), "lang": lang}
                return {"role": "doctor", "response": self._ask_age(lang), "lang": lang}
            return {"role": "doctor", "response": self._ask_name(lang), "lang": lang}

        # Stage 2: Ask for age
        if self.stage == "ask_age":
            if not self.patient_info.get("age"):
                # If patterns didn't catch age, try treating input as raw number
                age_match = re.search(r"(\d+)", user_message)
                if age_match:
                    self.patient_info["age"] = age_match.group(1)
            if self.patient_info.get("age"):
                self.stage = "consult"
                return {"role": "doctor", "response": self._ask_concern(lang), "lang": lang}
            return {"role": "doctor", "response": self._ask_age(lang), "lang": lang}

        # Stage 3: Normal consultation
        detected_symptoms = self.extract_symptoms(user_message)
        lower = user_message.lower().strip()
        is_prescription_req = self._is_prescription_request(user_message)
        is_surg_query = any(t in lower for t in [" surgery ", " operation ", " surgeri "])

        # Always update reported_symptoms when symptoms are detected
        if detected_symptoms:
            self.reported_symptoms = detected_symptoms

        if self.detect_danger(user_message):
            result = self._emergency_response(lang)
        elif is_surg_query and any(s in lower for s in SURGERY_INFO):
            surg_name = next(s for s in SURGERY_INFO if s in lower)
            info = self.get_surgery_info(surg_name, lang)
            if info:
                result = {"response": info, "lang": lang}
            else:
                result = self._ai_respond(user_message, lang)
        elif is_prescription_req:
            self.stage = "advised"
            if self.last_ai_advice:
                result = {"response": self.last_ai_advice, "lang": lang}
            elif self.reported_symptoms:
                result = self._give_advice(self.reported_symptoms, lang)
            else:
                result = self._ai_respond(user_message, lang)
            if isinstance(result, dict):
                self.last_ai_advice = result.get("response", "")
        elif self.use_ai:
            result = self._ai_respond(user_message, lang)
            if isinstance(result, dict):
                self.last_ai_advice = result.get("response", "")
                if self.last_ai_advice and self.stage != "advised":
                    self.stage = "advised"
            # Back-fill symptoms from AI response + user conversation
            if not self.reported_symptoms:
                # Check AI's own response for symptom keywords
                if isinstance(result, dict):
                    ai_text = result.get("response", "")
                    self.extract_symptoms(ai_text)
                    if self.current_symptoms:
                        self.reported_symptoms = list(set(self.reported_symptoms + self.current_symptoms))
                # Also re-check all user messages
                if not self.reported_symptoms:
                    for m in self.conversation_history:
                        if m["role"] == "user":
                            self.extract_symptoms(m["message"])
                            if self.current_symptoms:
                                self.reported_symptoms = list(set(self.reported_symptoms + self.current_symptoms))
                if self.reported_symptoms:
                    self.stage = "symptom_reported"
            # Even if no DB match, mark as advised so PDF button shows
            if not self.reported_symptoms and self.stage != "advised":
                self.stage = "symptom_reported"
        elif not detected_symptoms and self.stage == "consult" and not self.greeted:
            self.greeted = True
            result = self._greeting_response(lang)
        elif not detected_symptoms and self.stage == "consult":
            result = self._ask_symptoms(lang)
        elif not detected_symptoms and self.stage != "consult":
            result = self._handle_follow_up_answer(lang)
        else:
            if not self.greeted:
                self.greeted = True
            if detected_symptoms:
                self.reported_symptoms = detected_symptoms
            result = self._handle_symptoms(detected_symptoms, lang)

        if isinstance(result, dict):
            result["role"] = "doctor"
            if not self.last_ai_advice and result.get("response"):
                self.last_ai_advice = result["response"]
        return result

    def generate_consultation_summary(self, lang="en"):
        """Generate a summary of the consultation for prescription."""
        from .prescription_gen import PrescriptionGenerator
        rx = PrescriptionGenerator(
            patient_name=self.patient_info.get("name", "Patient"),
            lang=lang
        )
        if self.reported_symptoms:
            for sym_id in self.reported_symptoms:
                if sym_id in SYMPTOMS_DB:
                    meds = SYMPTOMS_DB[sym_id].get("medicines", [])
                    if meds:
                        primary = meds[0]
                        rx.add_medicine(
                            primary["name"],
                            primary["dosage"],
                            timing="as needed" if "emergency" in primary.get("line", "") else "as directed",
                            note=f"First-line option"
                        )
                    if lang == "hi":
                        rx.add_advice(" - ".join(SYMPTOMS_DB[sym_id]["home_remedies"]["hi"][:2]))
                    else:
                        rx.add_advice(" - ".join(SYMPTOMS_DB[sym_id]["home_remedies"]["en"][:2]))
        else:
            rx.add_advice("Consult a qualified doctor.")
        tests = {
            "fever": ["CBC", "Malaria/PCR", "Widal"],
            "headache": ["BP check", "CT/MRI brain (if severe)"],
            "chest_pain": ["ECG", "Troponin", "Chest X-ray"],
            "cough_cold": ["CBC", "Chest X-ray"],
            "acidity": ["Upper GI endoscopy"],
            "back_pain": ["X-ray spine", "MRI lumbar"],
            "skin_rash": ["Skin biopsy", "CBC"],
            "kidney_stone": ["USG KUB", "Urine R/M"],
            "high_bp": ["Lipid profile", "ECG", "KFT"],
            "diabetes": ["FBS/PPBS", "HbA1c"],
            "diarrhea": ["Stool R/M", "Stool culture"],
            "depression": ["PHQ-9", "Thyroid profile"],
            "anxiety": ["GAD-7", "Thyroid profile"],
        }
        for sym_id in self.reported_symptoms:
            for t in tests.get(sym_id, [])[:2]:
                rx.add_investigation(t)
        if lang == "hi":
            rx.set_follow_up("1 सप्ताह में दोबारा मिलें या लक्षण बिगड़ने पर तुरंत")
        else:
            rx.set_follow_up("Review in 1 week or sooner if symptoms worsen")
        return rx.generate_markdown()

    def get_specialist_referral(self, lang="en"):
        """Suggest the right specialist based on symptoms."""
        if not self.reported_symptoms:
            return None
        specialty_id = self.identify_specialty(self.reported_symptoms)
        spec = SPECIALTIES.get(specialty_id, SPECIALTIES["general"])
        name_en = spec["name_en"]
        name_hi = spec["name_hi"]
        if lang == "hi":
            return f"👉 **सुझाव:** कृपया **{name_hi}** विशेषज्ञ से सलाह लें।"
        return f"👉 **Recommendation:** Please consult a **{name_en}** specialist."

    def generate_prescription_pdf(self, lang="en"):
        """Generate a downloadable PDF prescription."""
        from .prescription_gen import PrescriptionGenerator
        pg = PrescriptionGenerator(
            patient_name=self.patient_info.get("name", "Patient"),
            patient_age=self.patient_info.get("age", ""),
            patient_weight=self.patient_info.get("weight", ""),
            lang=lang
        )

        # AI mode: use last AI chat response as prescription content
        ai_generated = False
        if self.use_ai and AI_AVAILABLE and self.last_ai_advice:
            pg.add_advice(self.last_ai_advice)
            ai_generated = True

        if not ai_generated:
            # KB-based fallback
            if self.reported_symptoms:
                for sym_id in self.reported_symptoms:
                    if sym_id in SYMPTOMS_DB:
                        sd = SYMPTOMS_DB[sym_id]
                        meds = sd.get("medicines", [])
                        if meds:
                            primary = meds[0]
                            pg.add_medicine(primary["name"], primary["dosage"],
                                            timing="as directed",
                                            note=f"First-line option. Alternatives: {', '.join(m['name'] for m in meds[1:3])}")
                        advice = sd.get("home_remedies", {}).get("en" if lang == "en" else "hi", [])
                        for a in advice[:3]:
                            pg.add_advice(a)
            else:
                if self.last_ai_advice:
                    sentences = [s.strip() for s in self.last_ai_advice.replace("•", ".").replace("\n", ".").split(".") if s.strip()]
                    for s in sentences[:4]:
                        pg.add_advice(s)
                else:
                    pg.add_advice("Consult a qualified doctor for proper diagnosis and treatment.")
                    pg.add_advice("Do not self-medicate without professional advice.")
                    pg.add_advice("Maintain a healthy lifestyle: balanced diet, exercise, adequate sleep.")
            tests_map = {
                "fever": ["CBC", "Malaria/PCR", "Urine R/M"], "headache": ["BP check", "CT/MRI brain"],
                "chest_pain": ["ECG", "Troponin", "Chest X-ray"], "cough_cold": ["CBC", "Chest X-ray"],
                "acidity": ["Upper GI endoscopy"], "back_pain": ["X-ray spine", "MRI lumbar"],
                "skin_rash": ["Skin biopsy", "CBC"], "kidney_stone": ["USG KUB", "Urine R/M"],
                "high_bp": ["Lipid profile", "ECG", "KFT"], "diabetes": ["FBS/PPBS", "HbA1c"],
                "diarrhea": ["Stool R/M", "Stool culture"], "depression": ["PHQ-9", "Thyroid profile"],
                "anxiety": ["GAD-7", "Thyroid profile"], "uti": ["Urine R/M", "Urine Culture"],
                "joint_pain": ["X-ray joint", "Uric acid", "RA factor"],
                "eye_infection": ["Eye swab culture"], "ear_infection": ["Ear swab culture"],
                "constipation": ["No tests usually needed"], "insomnia": ["No specific tests"],
                "fatigue": ["CBC", "Vitamin B12", "Vitamin D", "Thyroid"],
                "menstrual_cramps": ["USG pelvis"], "nausea_vomiting": ["CBC", "Stool exam"],
                "allergy": ["IgE levels", "Allergy panel"],
            }
            for sym_id in self.reported_symptoms:
                for t in tests_map.get(sym_id, [])[:3]:
                    pg.add_investigation(t)
            if lang == "hi":
                pg.set_follow_up("1 सप्ताह में दोबारा मिलें। लक्षण बिगड़ें तो तुरंत डॉक्टर से संपर्क करें।")
            else:
                pg.set_follow_up("Review in 1 week. Contact doctor immediately if symptoms worsen.")
        return pg.generate_pdf()

    def _build_patient_context(self):
        parts = []
        if self.patient_info.get("name"):
            parts.append(f"Patient name: {self.patient_info['name']}")
        if self.patient_info.get("age"):
            parts.append(f"Age: {self.patient_info['age']}")
        if self.patient_info.get("gender"):
            parts.append(f"Gender: {self.patient_info['gender']}")
        if self.reported_symptoms:
            sym_names = []
            for s in self.reported_symptoms:
                sd = SYMPTOMS_DB.get(s, {})
                sym_names.append(sd.get("en", [s])[0] if sd else s)
            parts.append(f"Reported symptoms: {', '.join(sym_names)}")
        if self.stage == "advised":
            parts.append("Stage: Already given initial advice")
        elif self.stage == "symptom_reported":
            parts.append(f"Stage: Gathering follow-up info (question {self.follow_up_count + 1})")
        return "\n".join(parts) if parts else "New patient, no info yet."

    def _ai_respond(self, user_message, lang):
        try:
            context = self._build_patient_context()
            is_req = self._is_prescription_request(user_message)
            if is_req and self.reported_symptoms:
                context += "\n\n**IMPORTANT: Patient is asking for prescription. STOP asking questions. Give prescription now.**"
            sys_prompt = (
                "You are Dr. Aarogya, an AI medical assistant. Talk like a real experienced doctor - "
                "warm, empathetic, and professional. Use natural conversation, not robotic.\n\n"
                f"Patient Context:\n{context}\n\n"
                "Guidelines:\n"
                "- If patient asks for prescription (prescription do / parcha do / give me medicine), "
                "STOP asking questions and give the prescription immediately\n"
                "- Ask only 1 follow-up question maximum, then give advice\n"
                "- Give concise advice (4-6 sentences max). Include home remedies when safe\n"
                "- Suggest relevant tests (CT scan, MRI, blood tests, etc.)\n"
                "- Recommend OTC medicines like Paracetamol, Ibuprofen, Cetirizine when safe\n"
                "- For prescription drugs, prescribe them directly with proper name, dosage, and duration. Always include a disclaimer: 'Consult a doctor before taking this medicine.'\n"
                "- Only recommend emergency care for TRUE emergencies: difficulty breathing, severe bleeding, unconsciousness, chest pain with sweating, major trauma\n"
                "- For minor bumps, bruises, or possible mild head injuries: stay calm, advise ice pack, rest, and monitoring. Do NOT send to ER unless symptoms are severe.\n"
                f"Respond in {'Hinglish (Hindi-English mix)' if lang == 'hi' else 'English'} naturally.\n"
                "Never use 'abe', 'yaar', 'bhai', 'arre'."
            )
            messages = [{"role": "system", "content": sys_prompt}]
            for m in self.conversation_history[-10:]:
                role = "user" if m["role"] == "user" else "assistant"
                messages.append({"role": role, "content": m["message"]})
            messages.append({"role": "user", "content": user_message})
            response = AI_CLIENT.chat.completions.create(
                model=AI_MODEL,
                messages=messages,
                max_tokens=800,
                temperature=0.7
            )
            text = response.choices[0].message.content.strip()
            self.conversation_history.append({"role": "assistant", "message": text, "lang": lang})
            return {"response": text, "lang": lang}
        except Exception as e:
            return self._fallback_response(lang)

    def _handle_symptoms(self, symptoms, lang):
        syms = symptoms if symptoms else self.reported_symptoms
        if not syms:
            return self._ask_symptoms(lang)

        if self.stage == "new" or self.stage == "advised" or (
            self.stage == "symptom_reported" and symptoms and symptoms != self.reported_symptoms):
            self.stage = "symptom_reported"
            self.follow_up_count = 0
            return self._ask_follow_up(syms, lang)

        if self.stage == "symptom_reported" and self.follow_up_count < 1:
            self.follow_up_count += 1
            return self._ask_follow_up(syms, lang)

        self.stage = "advised"
        return self._give_advice(syms, lang)

    def _handle_follow_up_answer(self, lang):
        self.follow_up_count += 1
        syms = self.reported_symptoms if self.reported_symptoms else self.current_symptoms
        if self.follow_up_count >= 1:
            self.stage = "advised"
            return self._give_advice(syms, lang)
        return self._ask_follow_up(syms, lang)

    def _ask_follow_up(self, symptoms, lang):
        sym_id = symptoms[0] if symptoms else None
        questions = FOLLOW_UP_QUESTIONS.get(sym_id, FOLLOW_UP_QUESTIONS.get("fever"))
        qs = questions["hi" if lang == "hi" else "en"]

        idx = self.follow_up_count
        if idx < len(qs):
            question = qs[idx]
        else:
            question = qs[0]

        if lang == "hi":
            sym_name = SYMPTOMS_DB[sym_id]["hi"] if sym_id and sym_id in SYMPTOMS_DB else SYMPTOMS_DB[symptoms[0]]["hi"]
            response = f"ठीक है। आपने {sym_name} बताया।\n\n{question}"
        else:
            sym_name = sym_id.replace("_", " ") if sym_id else "this"
            response = f"Okay. You mentioned {sym_name}.\n\n{question}"

        return {"response": response, "lang": lang}

    def _give_advice(self, symptoms, lang):
        sym_id = symptoms[0] if symptoms else "fever"
        if sym_id not in SYMPTOMS_DB:
            return self._fallback_response(lang)

        sym_data = SYMPTOMS_DB[sym_id]
        idx = 0 if lang == "en" else 1
        hi = lang == "hi"

        if hi:
            lines = ["समझ गया। आपकी परेशानी के बारे में।"]
            causes = sym_data["possible_causes"]["hi"]
            lines.append(f"\n**संभावित कारण:**")
            for c in causes[:3]:
                lines.append(f"• {c}")
            remedies = sym_data["home_remedies"]["hi"]
            lines.append(f"\n**घरेलू उपाय:**")
            for r in remedies[:3]:
                lines.append(f"✅ {r}")
            meds = sym_data.get("medicines", [])
            if meds:
                mild_med = meds[0]
                lines.append(f"\n**दवा (ज़रूरत हो तो):**")
                lines.append(f"💊 {mild_med['name']} - {mild_med['dosage']}")
                lines.append(f"\n*ध्यान दें: पहले डॉक्टर से सलाह लें*")
            red_flags = sym_data.get("red_flags", {}).get("hi", [])
            if red_flags and idx == 1:
                lines.append(f"\n⚠️ **सावधान:**")
                for rf in red_flags[:2]:
                    lines.append(f"• {rf}")
            lines.append(f"\n*और पूछना चाहते हैं कुछ?*")
        else:
            lines = ["I understand. Here is what I can suggest."]
            causes = sym_data["possible_causes"]["en"]
            lines.append(f"\n**Possible causes:**")
            for c in causes[:3]:
                lines.append(f"• {c}")
            remedies = sym_data["home_remedies"]["en"]
            lines.append(f"\n**Home care:**")
            for r in remedies[:3]:
                lines.append(f"✅ {r}")
            meds = sym_data.get("medicines", [])
            if meds:
                mild_med = meds[0]
                lines.append(f"\n**Medicine (if needed):**")
                lines.append(f"💊 {mild_med['name']} - {mild_med['dosage']}")
                lines.append(f"\n*Consult a doctor before use*")
            red_flags = sym_data.get("red_flags", {}).get("en", [])
            if red_flags:
                lines.append(f"\n⚠️ **Note:**")
                for rf in red_flags[:2]:
                    lines.append(f"• {rf}")
            lines.append(f"\n*Anything else you want to ask?*")

        tests = {
            "fever": ["CBC", "Malaria/PCR", "Widal test", "Urine R/M"],
            "headache": ["BP check", "CT/MRI brain (if severe)", "Eye checkup"],
            "cough_cold": ["CBC", "Chest X-ray", "Sputum culture"],
            "chest_pain": ["ECG", "Troponin test", "Chest X-ray", "Lipid profile"],
            "acidity": ["Upper GI endoscopy", "H. pylori test"],
            "back_pain": ["X-ray spine", "MRI lumbar (if severe)"],
            "skin_rash": ["Skin biopsy", "Patch test", "CBC"],
            "kidney_stone": ["USG KUB", "Urine R/M", "CT KUB", "Serum Creatinine"],
            "high_bp": ["BP monitoring", "Lipid profile", "ECG", "Kidney function test"],
            "diabetes": ["FBS/PPBS", "HbA1c", "OGTT"],
            "diarrhea": ["Stool R/M", "Stool culture", "CBC"],
            "depression": ["PHQ-9 score", "Thyroid profile", "Vitamin D"],
            "anxiety": ["GAD-7 score", "Thyroid profile", "ECG"],
        }
        test_list = tests.get(sym_id, [])
        if test_list:
            if hi:
                lines.append(f"\n🩸 **सुझाए गए टेस्ट:**")
                for t in test_list[:3]:
                    lines.append(f"• {t}")
            else:
                lines.append(f"\n🩸 **Suggested tests:**")
                for t in test_list[:3]:
                    lines.append(f"• {t}")

        response = "\n".join(lines)

        return {"response": response, "lang": lang, "symptoms": symptoms}

    def _greeting_response(self, lang):
        greeting = random.choice(GREETINGS["hi"] if lang == "hi" else GREETINGS["en"])
        return {"response": greeting, "lang": lang}

    def _ask_symptoms(self, lang):
        if lang == "hi":
            return {"response": "अपनी समस्या बताएं - जैसे सिरदर्द, बुखार, पेट दर्द, खांसी आदि।", "lang": lang}
        return {"response": "Tell me your concern - like headache, fever, stomach pain, cough etc.", "lang": lang}

    def _emergency_response(self, lang):
        if lang == "hi":
            return {
                "response": (
                    "🚨 **आपातकाल!** तुरंत डॉक्टर से मिलें या 108/102 पर कॉल करें।\n\n"
                    "यह AI सलाह है। बिना देर किए मेडिकल हेल्प लें।"
                ),
                "lang": lang,
                "emergency": True
            }
        return {
            "response": (
                "🚨 **EMERGENCY!** See a doctor immediately or call 911.\n\n"
                "This is AI advice. Get medical help without delay."
            ),
            "lang": lang,
            "emergency": True
        }

    def _fallback_response(self, lang):
        if lang == "hi":
            return {"response": "कृपया अपने लक्षण बताएं जैसे बुखार, खांसी, सिरदर्द, पेट दर्द आदि।", "lang": lang}
        return {"response": "Please describe your symptoms like fever, cough, headache, stomach pain etc.", "lang": lang}

    def get_medicine_info(self, medicine_name, lang="en"):
        name_lower = medicine_name.lower().strip()
        for med_id, med_data in MEDICINES_DB.items():
            if med_id in name_lower or any(b.lower() in name_lower for b in med_data["brands"]):
                info = []
                info.append(f"**{med_data['generic']}**")
                info.append(f"**Brands:** {', '.join(med_data['brands'])}")
                info.append(f"\n**Uses:**")
                for use in med_data["uses"]["en" if lang == "en" else "hi"]:
                    info.append(f"  • {use}")
                info.append(f"\n**Dosage:**")
                info.append(f"  {med_data['dosage']['en' if lang == 'en' else 'hi']}")
                info.append(f"\n**Side Effects:**")
                for se in med_data["side_effects"]["en" if lang == "en" else "hi"]:
                    info.append(f"  ⚠️ {se}")
                info.append(f"\n**Contraindications:**")
                for ci in med_data["contraindications"]["en" if lang == "en" else "hi"]:
                    info.append(f"  ✗ {ci}")
                info.append(f"\n**NB:** Visit your doctor before use.")
                return "\n".join(info)
        return None

    def get_surgery_info(self, surgery_type, lang="en"):
        name_lower = surgery_type.lower().strip()
        for surg_id, surg_data in SURGERY_INFO.items():
            if surg_id in name_lower:
                idx = 0 if lang == "en" else 1
                info = []
                info.append(f"**{list(surg_data.values())[idx]}**")
                info.append(f"\n{list(surg_data['details'].values())[idx]}")
                return "\n".join(info)
        return None


HinglishProcessor.PATTERNS = {
    "symptom_modifier": [
        (r"\b(tiz|tej|tez)\b", "severe"),
        (r"\b(halka|hulka)\b", "mild"),
        (r"\b(bohot|bahut|badhi)\b", "very"),
        (r"\b(kam|thoda)\b", "little"),
        (r"\b(lagatar|lagaathar)\b", "continuous"),
    ],
    "body_part": [
        (r"\b(khansi)\b", "cough"),
        (r"\b(bukhar|taap)\b", "fever"),
        (r"\b(dard)\b", "pain"),
        (r"\b(pet)\b", "stomach"),
        (r"\b(kamar)\b", "back"),
        (r"\b(sir|sar)\b", "head"),
        (r"\b(dil)\b", "heart"),
        (r"\b(aankh|ankh)\b", "eye"),
        (r"\b(kaan|kaano)\b", "ear"),
        (r"\b(naak)\b", "nose"),
        (r"\b(gala|gale)\b", "throat"),
    ]
}
