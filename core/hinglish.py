import re

HINGLISH_KEYWORDS = {
    "hello": "namaste",
    "fever": "bukhar",
    "headache": "sir dard",
    "stomach": "pet",
    "pain": "dard",
    "cough": "khansi",
    "cold": "zukaam",
    "medicine": "dawai",
    "doctor": "doctor",
    "surgery": "surgery / shalya chikitsa",
    "operation": "opereshan",
    "hospital": "aspatal",
    "knee": "ghutna",
    "back": "kamar",
    "eye": "aankh",
    "ear": "kaan",
    "nose": "naak",
    "throat": "gala",
    "leg": "pair",
    "hand": "haath",
    "chest": "seen",
    "heart": "dil",
}

LEVELS = {
    "hi_common": [
        (r'\b(mujhe|mera|meri|mere|mujh)\b', 'i'),
        (r'\b(tum|aap|tumhara|aapka)\b', 'you'),
        (r'\b(hai|hain|ho|hu|thi)\b', 'is/are'),
        (r'\b(ka|ke|ki|ko|se|mein|par|tak|tah)\b', 'of/to/from/in/on'),
        (r'\b(nahi|na|mat|manna)\b', 'no/not'),
        (r'\b(haan|haa|ji|haji)\b', 'yes'),
        (r'\b(achha|theek|tik)\b', 'okay/good'),
        (r'\b(kya|kyu|kab|kaise|kahan|kaun|kitna)\b', 'what/why/when/how/where/who/how much'),
        (r'\b(bukhar|taap|garami)\b', 'fever'),
        (r'\b(khansi|khans)\b', 'cough'),
        (r'\b(sir|sar)\b', 'head'),
        (r'\b(dard|darad|pira)\b', 'pain'),
        (r'\b(pet|paet)\b', 'stomach'),
        (r'\b(kamar|kamra)\b', 'back/waist'),
        (r'\b(ghutna|ghutane)\b', 'knee'),
        (r'\b(kaan|kann)\b', 'ear'),
        (r'\b(naak|nak)\b', 'nose'),
        (r'\b(gala|gale)\b', 'throat'),
        (r'\b(aankh|aankhen|ankh)\b', 'eye'),
        (r'\b(haath|hath)\b', 'hand'),
        (r'\b(pair|per)\b', 'leg/foot'),
        (r'\b(chamdi|tvacha)\b', 'skin'),
        (r'\b(dawai|dava)\b', 'medicine'),
        (r'\b(khana|khaana|bhojan)\b', 'food/meal'),
        (r'\b(pani|jAL)\b', 'water'),
        (r'\b(nendh|nind|neend)\b', 'sleep'),
        (r'\b(thakaan|thakavat)\b', 'fatigue/tiredness'),
        (r'\b(ultti|ulti|vomiting)\b', 'vomiting'),
        (r'\b(dast|pakhala|dast kholna)\b', 'diarrhea'),
        (r'\b(kabj|kabaj)\b', 'constipation'),
        (r'\b(gas|gass)\b', 'gas/acidity'),
        (r'\b(jor|jor ka)\b', 'loud/intense'),
        (r'\b(dil|dil)\b', 'heart'),
        (r'\b(jigar|kaleja)\b', 'liver'),
        (r'\b(gurda|gurde)\b', 'kidney'),
        (r'\b(phephda|phephde)\b', 'lung'),
        (r'\b(dimag|dimak)\b', 'brain'),
        (r'\b(saans|sans)\b', 'breath'),
        (r'\b(doctor|daaktr|vaidya)\b', 'doctor'),
        (r'\b(aspatal|hospital|nursing home)\b', 'hospital'),
        (r'\b(opereshan|surgery|shalya|shalya karm)\b', 'surgery'),
        (r'\b(frakture|fracture|haddi tutna)\b', 'fracture'),
        (r'\b(daane|rash|kharish|kharuj)\b', 'rash/itching'),
        (r'\b(sujan|soojan)\b', 'swelling'),
        (r'\b(chot|chott|sot)\b', 'injury'),
        (r'\b(khoon|khuun|rakat)\b', 'blood'),
        (r'\b(bp|blood pressure)\b', 'bp'),
        (r'\b(shugar|sugar|shakkar)\b', 'sugar/diabetes'),
        (r'\b(sardi|cold|thand)\b', 'cold'),
        (r'\b(jukam|zukaam)\b', 'cold/runny nose'),
        (r'\b(seeks|hik|sikun)\b', 'learning'),
        (r'\b(raat|rat)\b', 'night'),
        (r'\b(shaam|sham)\b', 'evening'),
        (r'\b(sabah|subah)\b', 'morning'),
        (r'\b(aaj)\b', 'today'),
        (r'\b(kal)\b', 'yesterday/tomorrow'),
        (r'\b(kitne)\b', 'how many'),
        (r'\b(din)\b', 'day'),
        (r'\b(hapta|hafte)\b', 'week'),
        (r'\b(mahina|mahine)\b', 'month'),
        (r'\b(saal|saal)\b', 'year'),
        (r'\b(umr|umar)\b', 'age'),
        (r'\b(vajan|vajan|weight)\b', 'weight'),
    ]
}

HINGLISH_PATTERNS = {
    "body_part": [
        (r"\b(khyansi|khansi|khans)\b", "cough"),
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
    ],
    "symptom_modifier": [
        (r"\b(tiz|tej|tez)\b", "severe"),
        (r"\b(halka|hulka)\b", "mild"),
        (r"\b(bohot|bahut|badhi)\b", "very"),
        (r"\b(kam|thoda)\b", "little"),
        (r"\b(lagatar|lagaathar)\b", "continuous"),
    ],
    "time_indicators": [
        (r"\b(kitne din)\b", "how many days"),
        (r"\b(kab se)\b", "since when"),
        (r"\b(subah|subeh)\b", "morning"),
        (r"\b(raat)\b", "night"),
        (r"\b(shaam)\b", "evening"),
    ]
}

LANG_COMMON_WORDS = {
    "en": {"the", "a", "an", "is", "are", "was", "were", "be", "been", "have", "has", "had",
           "do", "does", "did", "will", "would", "shall", "should", "can", "could", "may", "might",
           "in", "on", "at", "to", "for", "with", "by", "from", "of", "and", "or", "but",
           "i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them",
           "my", "your", "his", "its", "our", "their", "mine", "yours", "theirs",
           "this", "that", "these", "those", "please", "thank", "yes", "no", "not",
           "hello", "hi", "hey"},
    "hi": {"hai", "hain", "ho", "hu", "thi", "ka", "ke", "ki", "ko", "se",
           "mein", "par", "tak", "aur", "ya", "lekin", "is", "us", "in", "un", "yeh", "woh",
           "mujhe", "tum", "aap", "main", "hum", "mera", "tera", "aapka", "iska", "uska",
           "kya", "kyun", "kab", "kaise", "kahan", "kaun", "kis", "kitna",
           "haan", "nahi", "na", "mat", "ji", "haji", "achha", "theek"}
}


class HinglishProcessor:
    def __init__(self):
        pass

    def detect_language(self, text):
        text_lower = text.lower().strip()
        words = set(re.findall(r'\b[a-z]+\b', text_lower))
        if not words:
            return "unknown"

        en_count = len(words & LANG_COMMON_WORDS["en"])
        hi_count = len(words & LANG_COMMON_WORDS["hi"])
        has_devanagari = bool(re.search(r'[\u0900-\u097F]', text))
        hi_roman_count = 0
        matched_words = set()
        for _, hindi_word in HINGLISH_KEYWORDS.items():
            hw = hindi_word.split("/")[0].split("(")[0].strip()
            if hw and hw in text_lower and hw not in matched_words:
                matched_words.add(hw)
                hi_roman_count += 1

        for pattern_list in LEVELS.values():
            for p, _ in pattern_list:
                m = re.search(p, text_lower, re.IGNORECASE)
                if m:
                    matched = m.group(0)
                    if matched not in matched_words:
                        matched_words.add(matched)
                        hi_roman_count += 1

        if has_devanagari:
            return "hi"
        if hi_count > 0 or (hi_roman_count >= 2 and hi_roman_count > en_count):
            return "hi"
        if en_count > 0:
            return "en"
        if hi_roman_count == 1 and en_count == 0:
            return "en"
        if hi_roman_count > 0:
            return "hi"
        return "en"

    def translate_hinglish_to_en(self, text):
        text_lower = text.lower()
        for pattern_list in LEVELS.values():
            for p, replacement in pattern_list:
                text_lower = re.sub(p, replacement, text_lower, flags=re.IGNORECASE)
        return text_lower

    def get_bilingual_response(self, en_text, hi_text, lang):
        if lang == "hi":
            return hi_text if hi_text else en_text
        return en_text
