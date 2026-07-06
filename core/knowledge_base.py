SOURCES = {
    "mayo_clinic_tension_headache": "Mayo Clinic - Tension Headache: Diagnosis & Treatment (https://www.mayoclinic.org/diseases-conditions/tension-headache/diagnosis-treatment/drc-20353982)",
    "nih_medlineplus_headache": "NIH MedlinePlus - Headache (https://medlineplus.gov/headache.html)",
    "nih_news_health_headache": "NIH News in Health - Tension Headaches, Migraine & More (Sept 2025)",
    "ihs_migraine_guidelines_2025": "IHS Evidence-Based Guidelines for Pharmacological Treatment of Migraine (2025) - Cephalalgia",
    "ahs_ed_migraine_2025": "American Headache Society - 2025 Guideline Update: Acute Treatment of Migraine in ED (Headache journal)",
    "uptodate_tth": "UpToDate - Tension-Type Headache in Adults: Acute Treatment (Lit review Nov 2025)",
    "bash_guidelines": "British Association for the Study of Headache - TTH Guidelines 2019",
    "nature_paracetamol_vs_ibuprofen": "Paracetamol vs Ibuprofen for ETTH - Systematic Review & Network Meta-analysis (Scientific Reports 2023)",
    "dfg_guidelines": "Deutsche Gesellschaft fur Neurologie - TTH Treatment Guidelines",
    "osf_pharmacist": "OSF HealthCare - Acetaminophen vs Ibuprofen: Which Should You Pick? (2025)",
    "boots_pain_guide": "Boots UK - Paracetamol & Ibuprofen Pain Relief Guide",
    "healthdirect_au": "HealthDirect Australia - Medicines for Headaches (May 2025)",
    "msu_medicine": "Michigan State University - Best Tension Headache Remedies (2026)",
    "cdsco_india": "DCGI India - Approved FDC Combinations",
    "who_essential_medicines": "WHO Model List of Essential Medicines",
    "icmr_india": "ICMR India - Standard Treatment Workflows",
    "cochrane_review": "Cochrane Database Syst Rev - Acute Treatment of TTH",
    "american_migraine_foundation": "American Migraine Foundation - Acute Therapy OTC Options",
    "nccih_nih": "NCCIH NIH - Headaches: What You Need to Know",
    "va_dod_headache": "VA/DoD Clinical Practice Guideline - Management of Headache (2023)",
    "caffeine_adjuvant": "Caffeine as analgesic adjuvant in tension headache - Clin Pharmacol Ther 1994",
}

SPECIALTIES = {
    "general": {
        "name_en": "General Medicine",
        "name_hi": "सामान्य चिकित्सा",
        "keywords": ["fever", "cold", "cough", "headache", "body pain", "weakness",
                     "bukhar", "khansi", "sir dard", "kamzori", "bukhaar"]
    },
    "cardiology": {
        "name_en": "Cardiology",
        "name_hi": "हृदय रोग",
        "keywords": ["chest pain", "heart", "bp", "blood pressure", "heart attack",
                     "seene mein dard", "dil", "haarts"]
    },
    "gastroenterology": {
        "name_en": "Gastroenterology",
        "name_hi": "गैस्ट्रोएंटरोलॉजी",
        "keywords": ["stomach", "acidity", "gas", "indigestion", "diarrhea", "constipation",
                     "pet", "pet dard", "gas", "kabj", "dast"]
    },
    "neurology": {
        "name_en": "Neurology",
        "name_hi": "न्यूरोलॉजी",
        "keywords": ["brain", "headache", "migraine", "dizziness", "paralysis", "seizure",
                     "dimag", "migrain", "chakkar", "mirgi"]
    },
    "orthopedics": {
        "name_en": "Orthopedics",
        "name_hi": "ऑर्थोपेडिक्स",
        "keywords": ["bone", "joint", "fracture", "back pain", "knee", "spine",
                     "haddi", "jod", "frakture", "kamar dard", "ghutna"]
    },
    "dermatology": {
        "name_en": "Dermatology",
        "name_hi": "त्वचा रोग",
        "keywords": ["skin", "rash", "infection", "acne", "allergy", "itch",
                     "chamdi", "daane", "kharish", "rash"]
    },
    "ophthalmology": {
        "name_en": "Ophthalmology",
        "name_hi": "नेत्र रोग",
        "keywords": ["eye", "vision", "red eye", "eye infection", "cataract",
                     "aankh", "aankhen", "nazar"]
    },
    "ent": {
        "name_en": "ENT",
        "name_hi": "कान, नाक, गला",
        "keywords": ["ear", "nose", "throat", "hearing", "tonsil", "sinus",
                     "kaan", "naak", "gala", "tonsils"]
    },
    "pulmonology": {
        "name_en": "Pulmonology",
        "name_hi": "फेफड़ा रोग",
        "keywords": ["lung", "breathing", "asthma", "pneumonia", "tb", "cough",
                     "phephda", "saans", "dama", "tb"]
    },
    "surgery": {
        "name_en": "Surgery",
        "name_hi": "शल्य चिकित्सा",
        "keywords": ["operation", "surgery", "appendicitis", "gallstone", "hernia",
                     "opereshan", "sarijri", "hernia"]
    },
    "psychiatry": {
        "name_en": "Psychiatry",
        "name_hi": "मनोरोग",
        "keywords": ["depression", "anxiety", "stress", "insomnia", "mental",
                     "udaas", "ghabrahat", "tanav", "nendh"]
    },
    "nephrology": {
        "name_en": "Nephrology",
        "name_hi": "गुर्दा रोग",
        "keywords": ["kidney", "urine", "stone", "infection uti",
                     "gurda", "peshab", "pathri"]
    }
}

SYMPTOMS_DB = {
    "fever": {
        "en": ["fever", "high temperature", "body hot", "bukhar", "taap"],
        "hi": "बुखार",
        "description": {
            "en": "Fever is a temporary increase in body temperature, often due to an illness.",
            "hi": "बुखार शरीर के तापमान का अस्थायी बढ़ना है, जो अक्सर बीमारी के कारण होता है।"
        },
        "possible_causes": {
            "en": ["Viral infection (cold, flu, COVID-19)", "Bacterial infection", "Urinary tract infection",
                   "Dengue, Malaria (in endemic areas)", "Vaccination reaction", "Heat exhaustion"],
            "hi": ["वायरल संक्रमण (सर्दी, फ्लू, कोविड-19)", "जीवाणु संक्रमण", "मूत्र मार्ग संक्रमण",
                   "डेंगू, मलेरिया (स्थानिक क्षेत्रों में)", "टीकाकरण प्रतिक्रिया", "गर्मी से थकावट"]
        },
        "home_remedies": {
            "en": ["Rest and hydrate well", "Use cold compress on forehead", "Take paracetamol if temperature > 101°F",
                   "Monitor temperature every 4-6 hours", "Light clothing and cool environment"],
            "hi": ["आराम करें और पर्याप्त पानी पिएं", "माथे पर ठंडी पट्टी रखें", "यदि तापमान 101°F से अधिक हो तो पैरासिटामोल लें",
                   "हर 4-6 घंटे में तापमान जांचें", "हल्के कपड़े पहनें और ठंडे वातावरण में रहें"]
        },
        "medicines": [
            {"name": "Paracetamol", "dosage": "500-650 mg every 6 hours", "type": "tablet/syrup", "line": "first", "source": "WHO Essential Medicines, ICMR India STW"},
            {"name": "Ibuprofen", "dosage": "400 mg every 8 hours with food", "type": "tablet", "line": "first", "source": "WHO Essential Medicines"},
            {"name": "Mefenamic Acid", "dosage": "250-500 mg three times daily after food", "type": "tablet", "line": "second", "source": "ICMR India STW"},
        ],
        "red_flags": {
            "en": ["Temperature > 103°F not reducing with medicine", "Stiff neck", "Severe headache",
                   "Rash that doesn't blanch", "Difficulty breathing", "Confusion"],
            "hi": ["दवा से भी 103°F से अधिक बुखार कम न होना", "गर्दन में अकड़न", "तीव्र सिरदर्द",
                   "दबाने पर न मिटने वाले दाने", "सांस लेने में कठिनाई", "भ्रम की स्थिति"]
        },
        "needs_surgery": False
    },
    "headache": {
        "en": ["headache", "sir dard", "head pain", "migraine", "sardard"],
        "hi": "सिरदर्द",
        "description": {
            "en": "Headache is pain in any region of the head. Types include tension-type (most common), migraine, cluster, and secondary headaches due to other conditions.",
            "hi": "सिरदर्द सिर के किसी भी हिस्से में दर्द है। प्रकार: तनाव-प्रकार (सबसे आम), माइग्रेन, क्लस्टर, और अन्य स्थितियों के कारण द्वितीयक सिरदर्द।"
        },
        "possible_causes": {
            "en": ["Tension headache (stress, eye strain, poor posture)", "Migraine (often with nausea, light sensitivity)",
                   "Dehydration / Not drinking enough water", "Sinus infection / congestion",
                   "Cervical spine issues / neck tension", "High blood pressure",
                   "Medication overuse headache (painkillers > 3 days/week)", "Lack of sleep / Fatigue",
                   "Caffeine withdrawal", "Cluster headache (rare, severe, one-sided)"],
            "hi": ["तनाव सिरदर्द (तनाव, आंखों पर दबाव, खराब मुद्रा)", "माइग्रेन (अक्सर मतली, रोशनी से तकलीफ)",
                   "निर्जलीकरण / पर्याप्त पानी न पीना", "साइनस संक्रमण / जुकाम",
                   "गर्दन की समस्या / गर्दन में तनाव", "उच्च रक्तचाप",
                   "दवा अधिक उपयोग सिरदर्द (सप्ताह में 3 दिन से अधिक दर्द निवारक)", "नींद की कमी / थकान",
                   "कैफीन की कमी", "क्लस्टर सिरदर्द (दुर्लभ, तेज, एक तरफ)"]
        },
        "home_remedies": {
            "en": ["Rest in a dark, quiet room", "Apply cold or warm compress to head/neck",
                   "Stay well hydrated (6-8 glasses of water daily)", "Gentle massage of temples, neck, and shoulders",
                   "Avoid screen time for 30-60 min", "Peppermint oil application on temples (cooling effect)",
                   "Practice deep breathing / relaxation", "Keep a headache diary to identify triggers",
                   "Maintain regular sleep schedule"],
            "hi": ["अंधेरे, शांत कमरे में आराम करें", "सिर/गर्दन पर ठंडी या गर्म पट्टी रखें",
                   "पर्याप्त पानी पिएं (दिन में 6-8 गिलास)", "कनपटी और गर्दन की हल्की मालिश करें",
                   "30-60 मिनट स्क्रीन से दूर रहें", "पेपरमिंट ऑयल कनपटी पर लगाएं",
                   "गहरी सांस / ध्यान करें", "ट्रिगर पहचानने के लिए डायरी रखें",
                   "नियमित नींद का समय रखें"]
        },
        "medicines": [
            {"name": "Ibuprofen 400mg", "dosage": "400 mg every 6-8 hours with food (max 1200 mg/day)", "type": "tablet", "line": "first", "source": "Mayo Clinic; UpToDate; IHS Guidelines"},
            {"name": "Paracetamol 500-1000mg", "dosage": "500-1000 mg every 4-6 hours (max 4000 mg/day)", "type": "tablet", "line": "first", "source": "Mayo Clinic; WHO Essential Medicines"},
            {"name": "Aspirin 500-1000mg", "dosage": "500-1000 mg every 6 hours (max 4000 mg/day)", "type": "tablet", "line": "first", "source": "NICE Guidelines; DFG Guidelines"},
            {"name": "Naproxen Sodium 550mg", "dosage": "550 mg initially, then 275 mg after 6-8 hours", "type": "tablet", "line": "first", "source": "Mayo Clinic; UpToDate"},
            {"name": "Paracetamol + Caffeine (500mg + 65mg)", "dosage": "1-2 tablets at onset", "type": "tablet", "line": "first", "source": "Cochrane Review; Clin Pharmacol Ther 1994"},
            {"name": "Sumatriptan 50mg (for migraine)", "dosage": "50-100 mg at onset of migraine pain", "type": "tablet", "line": "second", "source": "IHS Migraine Guidelines 2025; AHS 2025"},
            {"name": "Diclofenac Potassium 50mg", "dosage": "50 mg three times daily with food", "type": "tablet", "line": "second", "source": "ICMR India STW; DFG Guidelines"},
        ],
        "red_flags": {
            "en": ["Sudden severe 'thunderclap' headache (worst of life)", "Headache with fever and stiff neck (possible meningitis)",
                   "Headache after head injury", "Headache with vision changes, slurred speech, or weakness",
                   "Headache with seizure", "Headache waking you from sleep (in elderly)"],
            "hi": ["अचानक तीव्र 'थंडरक्लैप' सिरदर्द (जीवन का सबसे बुरा)", "बुखार और गर्दन में अकड़न के साथ सिरदर्द (संभावित मेनिन्जाइटिस)",
                   "सिर में चोट के बाद सिरदर्द", "दृष्टि बदलने, बोलने में समस्या या कमजोरी के साथ सिरदर्द",
                   "दौरे के साथ सिरदर्द", "नींद से जगाने वाला सिरदर्द (बुजुर्गों में)"]
        },
        "needs_surgery": False,
        "medicine_notes": {
            "en": "For tension headaches: Ibuprofen or Paracetamol first-line. Ibuprofen may be more effective per some guidelines (DFG, UpToDate). For migraine: Sumatriptan or combination of Aspirin+Paracetamol+Caffeine. Avoid painkillers > 3 days/week to prevent medication overuse headache.",
            "hi": "तनाव सिरदर्द के लिए: पहले Ibuprofen या Paracetamol लें। कुछ गाइडलाइन्स के अनुसार Ibuprofen ज्यादा प्रभावी है। माइग्रेन के लिए: Sumatriptan या Aspirin+Paracetamol+Caffeine का कॉम्बिनेशन। दर्द निवारक सप्ताह में 3 दिन से ज्यादा न लें।"
        }
    },
    "chest_pain": {
        "en": ["chest pain", "seene mein dard", "heart pain", "chest discomfort"],
        "hi": "सीने में दर्द",
        "description": {
            "en": "Chest pain can be a sign of heart problems but also has many other causes.",
            "hi": "सीने में दर्द हृदय समस्या का संकेत हो सकता है लेकिन इसके कई अन्य कारण भी हैं।"
        },
        "possible_causes": {
            "en": ["Angina / Heart attack (medical emergency)", "GERD / Acidity", "Muscle strain",
                   "Costochondritis", "Anxiety / Panic attack", "Pulmonary issues"],
            "hi": ["एनजाइना / हार्ट अटैक (चिकित्सा आपातकाल)", "एसिडिटी / गैस", "मांसपेशियों में खिंचाव",
                   "कोस्टोकॉन्ड्राइटिस", "चिंता / पैनिक अटैक", "फेफड़ों की समस्या"]
        },
        "home_remedies": {
            "en": ["Seek immediate medical help - do not self-treat chest pain"],
            "hi": ["सीने के दर्द का स्व-उपचार न करें - तुरंत चिकित्सा सहायता लें"]
        },
        "medicines": [
            {"name": "Sorbitrate (for angina - emergency)", "dosage": "5 mg sublingual", "type": "tablet", "line": "emergency", "source": "AHA/ACC Guidelines"},
            {"name": "Aspirin 325mg (chewed, if heart attack suspected)", "dosage": "325 mg chewed immediately", "type": "tablet", "line": "emergency", "source": "AHA/ACC Guidelines"},
            {"name": "Antacids (if acidity-related)", "dosage": "as directed", "type": "tablet/syrup", "line": "first", "source": "ICMR India STW"},
        ],
        "red_flags": {
            "en": ["Any chest pain with sweating, nausea, shortness of breath",
                   "Pain radiating to left arm, jaw, or back", "Chest pain with dizziness"],
            "hi": ["पसीना, मतली, सांस फूलने के साथ सीने में दर्द",
                   "बाएं हाथ, जबड़े या पीठ में फैलने वाला दर्द", "चक्कर के साथ सीने में दर्द"]
        },
        "needs_surgery": True,
        "surgery_detail": {
            "en": "May require Angioplasty, CABG (bypass surgery), or stent placement based on severity. Source: AHA/ACC",
            "hi": "गंभीरता के आधार पर एंजियोप्लास्टी, CABG (बाइपास सर्जरी), या स्टेंट लगाने की आवश्यकता हो सकती है।"
        }
    },
    "acidity": {
        "en": ["acidity", "gas", "indigestion", "heartburn", "acid reflux", "pet mein jalan", "pet gas"],
        "hi": "एसिडिटी / गैस",
        "description": {
            "en": "Acidity occurs when stomach acid flows back into the esophagus causing burning sensation.",
            "hi": "एसिडिटी तब होती है जब पेट का एसिड वापस अन्नप्रणाली में आ जाता है जिससे जलन होती है।"
        },
        "possible_causes": {
            "en": ["Spicy/oily food", "Irregular eating habits", "Stress", "Hiatal hernia",
                   "Pregnancy", "Certain medications (NSAIDs)", "Obesity", "Smoking / Alcohol"],
            "hi": ["मसालेदार/तेल वाला खाना", "अनियमित खानपान", "तनाव", "हायटल हर्निया",
                   "गर्भावस्था", "कुछ दवाएं (NSAIDs)", "मोटापा", "धूम्रपान / शराब"]
        },
        "home_remedies": {
            "en": ["Eat small frequent meals", "Avoid spicy, oily, acidic food", "Don't lie down immediately after eating",
                   "Drink cold milk or buttermilk", "Chew fennel seeds after meals", "Elevate head while sleeping",
                   "Reduce caffeine and alcohol", "Maintain healthy weight"],
            "hi": ["छोटे-छोटे भोजन करें", "मसालेदार, तेल वाले भोजन से बचें", "खाने के तुरंत बाद न लेटें",
                   "ठंडा दूध या छाछ पिएं", "खाने के बाद सौंफ चबाएं", "सोते समय सिर ऊंचा रखें",
                   "कैफीन और शराब कम करें", "स्वस्थ वजन रखें"]
        },
        "medicines": [
            {"name": "Antacid Gel (Magnesium Hydroxide + Aluminium)", "dosage": "10-20 ml after meals and at bedtime", "type": "syrup", "line": "first", "source": "ICMR India STW; WHO"},
            {"name": "Pantoprazole", "dosage": "40 mg before breakfast (empty stomach)", "type": "tablet", "line": "first", "source": "WHO Essential Medicines; ICMR India STW"},
            {"name": "Ranitidine", "dosage": "150 mg twice daily before meals", "type": "tablet", "line": "first", "source": "WHO Essential Medicines"},
            {"name": "Domperidone (for nausea with reflux)", "dosage": "10 mg before meals", "type": "tablet", "line": "second", "source": "ICMR India STW"},
        ],
        "red_flags": {
            "en": ["Difficulty swallowing", "Blood in vomit", "Unexplained weight loss", "Severe persistent pain"],
            "hi": ["निगलने में कठिनाई", "उल्टी में खून", "बिना कारण वजन कम होना", "लगातार तेज दर्द"]
        },
        "needs_surgery": True,
        "surgery_detail": {
            "en": "In severe GERD cases, Fundoplication surgery may be recommended. Source: ASGE/SAGES Guidelines",
            "hi": "गंभीर GERD मामलों में फंडोप्लीकेशन सर्जरी की सिफारिश की जा सकती है।"
        }
    },
    "back_pain": {
        "en": ["back pain", "kamar dard", "lower back pain", "spine pain"],
        "hi": "पीठ दर्द / कमर दर्द",
        "description": {
            "en": "Back pain is very common and can range from mild to severe. It affects people of all ages.",
            "hi": "पीठ दर्द बहुत आम है और हल्के से गंभीर तक हो सकता है। यह सभी उम्र के लोगों को प्रभावित करता है।"
        },
        "possible_causes": {
            "en": ["Muscle strain or sprain", "Poor posture / prolonged sitting", "Herniated disc",
                   "Spinal stenosis", "Arthritis", "Sciatica", "Kidney stones or infection"],
            "hi": ["मांसपेशियों में खिंचाव", "खराब मुद्रा / लंबे समय तक बैठना", "डिस्क का खिसकना",
                   "रीढ़ की नली का सिकुड़ना", "गठिया", "सायटिका", "गुर्दे की पथरी या संक्रमण"]
        },
        "home_remedies": {
            "en": ["Apply hot/cold packs (alternate)", "Gentle stretching", "Maintain good posture",
                   "Sleep on a firm mattress", "Avoid heavy lifting", "Walk regularly (gentle movement helps)",
                   "Ergonomic chair support"],
            "hi": ["गर्म/ठंडी सिकाई करें (बारी-बारी)", "हल्का स्ट्रेचिंग करें", "अच्छी मुद्रा रखें",
                   "सख्त गद्दे पर सोएं", "भारी सामान उठाने से बचें", "नियमित रूप से टहलें",
                   "एर्गोनोमिक कुर्सी का उपयोग करें"]
        },
        "medicines": [
            {"name": "Paracetamol", "dosage": "500-650 mg every 6 hours", "type": "tablet", "line": "first", "source": "WHO"},
            {"name": "Diclofenac Gel 1% (Topical)", "dosage": "apply thin layer 3-4 times daily", "type": "gel", "line": "first", "source": "ICMR India; NICE Guidelines"},
            {"name": "Ibuprofen", "dosage": "400 mg every 8 hours with food", "type": "tablet", "line": "first", "source": "WHO; NICE"},
            {"name": "Thiocolchicoside (muscle relaxant)", "dosage": "8 mg twice daily", "type": "tablet", "line": "second", "source": "ICMR India STW"},
            {"name": "Methylcobalamin + Pregabalin (for nerve pain)", "dosage": "as prescribed", "type": "tablet", "line": "second", "source": "ICMR India STW"},
        ],
        "red_flags": {
            "en": ["Loss of bladder/bowel control (cauda equina syndrome)", "Numbness in legs",
                   "Pain after a fall/injury", "Fever with back pain", "Unexplained weight loss"],
            "hi": ["मूत्र/मल नियंत्रण खोना", "पैरों में सुन्नता", "गिरने/चोट के बाद दर्द",
                   "बुखार के साथ पीठ दर्द", "बिना कारण वजन कम होना"]
        },
        "needs_surgery": True,
        "surgery_detail": {
            "en": "Surgery options: Discectomy, Laminectomy, Spinal Fusion. Only after 6-8 weeks of failed conservative treatment or in emergency. Source: AAOS/NASS Guidelines",
            "hi": "सर्जरी विकल्प: डिस्केक्टॉमी, लैमिनेक्टॉमी, स्पाइनल फ्यूजन। केवल 6-8 सप्ताह के असफल उपचार के बाद या आपातकाल में।"
        }
    },
    "skin_rash": {
        "en": ["rash", "skin rash", "itching", "kharish", "red bumps", "hives"],
        "hi": "त्वचा पर दाने / खुजली",
        "description": {
            "en": "Skin rashes can be caused by allergies, infections, or other skin conditions.",
            "hi": "त्वचा पर दाने एलर्जी, संक्रमण या अन्य त्वचा स्थितियों के कारण हो सकते हैं।"
        },
        "possible_causes": {
            "en": ["Allergic reaction (food, medicine, pollen)", "Eczema (Atopic dermatitis)",
                   "Fungal infection (ringworm)", "Contact dermatitis", "Heat rash", "Psoriasis"],
            "hi": ["एलर्जी प्रतिक्रिया (खाना, दवा, पराग)", "एक्ज़िमा (एटॉपिक डर्मेटाइटिस)",
                   "फंगल संक्रमण (दाद)", "कॉन्टैक्ट डर्मेटाइटिस", "घमौरियां", "सोरायसिस"]
        },
        "home_remedies": {
            "en": ["Avoid scratching", "Apply calamine lotion", "Use cold compresses",
                   "Avoid known allergens", "Keep skin clean and dry", "Use mild, fragrance-free soap"],
            "hi": ["खुजली से बचें", "कैलामाइन लोशन लगाएं", "ठंडी सिकाई करें",
                   "ज्ञात एलर्जी से बचें", "त्वचा को साफ और सूखा रखें", "हल्का, बिना खुशबू वाला साबुन उपयोग करें"]
        },
        "medicines": [
            {"name": "Cetirizine", "dosage": "10 mg at night", "type": "tablet", "line": "first", "source": "WHO Essential Medicines"},
            {"name": "Hydrocortisone cream 1% (mild steroid)", "dosage": "apply thin layer 2-3 times daily, max 7 days", "type": "cream", "line": "first", "source": "NICE; ICMR India STW"},
            {"name": "Clotrimazole cream 1% (for fungal)", "dosage": "apply twice daily for 2-4 weeks", "type": "cream", "line": "first", "source": "WHO; ICMR India STW"},
            {"name": "Calamine Lotion", "dosage": "apply as needed for itching", "type": "lotion", "line": "first", "source": "OTC Standard"},
        ],
        "red_flags": {
            "en": ["Rash with fever", "Blisters on skin or mouth", "Rash spreading rapidly",
                   "Difficulty breathing/swelling of face", "Rash with joint pain"],
            "hi": ["बुखार के साथ दाने", "त्वचा या मुंह पर छाले", "तेजी से फैलने वाले दाने",
                   "सांस लेने में कठिनाई/चेहरे पर सूजन", "जोड़ों के दर्द के साथ दाने"]
        },
        "needs_surgery": False
    },
    "cough_cold": {
        "en": ["cough", "cold", "khansi", "zukaam", "runny nose", "sore throat", "gala dard"],
        "hi": "खांसी / जुकाम",
        "description": {
            "en": "Common cold is a viral infection of the upper respiratory tract. It's usually harmless.",
            "hi": "सामान्य सर्दी ऊपरी श्वसन पथ का एक वायरल संक्रमण है। यह आमतौर पर हानिरहित है।"
        },
        "possible_causes": {
            "en": ["Viral infection (Rhinovirus - most common)", "Allergies (hay fever)", "Bacterial infection (secondary)",
                   "COVID-19", "Influenza (Flu)", "Environmental irritants"],
            "hi": ["वायरल संक्रमण (राइनोवायरस - सबसे आम)", "एलर्जी (हे फीवर)", "जीवाणु संक्रमण (द्वितीयक)",
                   "कोविड-19", "इन्फ्लुएंजा (फ्लू)", "पर्यावरणीय जलन"]
        },
        "home_remedies": {
            "en": ["Warm water with honey and lemon", "Steam inhalation (add few drops of eucalyptus oil)",
                   "Gargle with warm salt water", "Drink warm soups and herbal teas",
                   "Take adequate rest", "Use saline nasal drops for congestion",
                   "Use humidifier in room"],
            "hi": ["शहद और नींबू के साथ गर्म पानी", "भाप लें (नीलगिरी के तेल की कुछ बूंदें डालें)",
                   "गर्म नमक वाले पानी से गरारे करें", "गर्म सूप और हर्बल चाय पिएं",
                   "पर्याप्त आराम करें", "नाक की भीड़ के लिए सेलाइन नेज़ल ड्रॉप्स",
                   "कमरे में ह्यूमिडिफायर का उपयोग करें"]
        },
        "medicines": [
            {"name": "Paracetamol (for fever/body ache)", "dosage": "500-650 mg as needed", "type": "tablet", "line": "first", "source": "WHO; ICMR India STW"},
            {"name": "Cetirizine (for runny nose/sneezing)", "dosage": "10 mg at night", "type": "tablet", "line": "first", "source": "WHO Essential Medicines"},
            {"name": "Pseudoephedrine (for nasal congestion)", "dosage": "60 mg every 6 hours", "type": "tablet", "line": "first", "source": "ICMR India STW"},
            {"name": "Dextromethorphan (for dry cough)", "dosage": "10-20 mg every 6-8 hours", "type": "syrup/tablet", "line": "first", "source": "ICMR India STW"},
            {"name": "Amoxicillin (if bacterial infection suspected)", "dosage": "500 mg three times daily - 5 days", "type": "capsule", "line": "second", "source": "WHO; ICMR India STW"},
            {"name": "Zinc lozenges (may reduce duration)", "dosage": "as directed", "type": "lozenge", "line": "supplement", "source": "Cochrane Review"},
        ],
        "red_flags": {
            "en": ["Fever > 101°F for more than 3 days", "Difficulty breathing", "Chest pain",
                   "Coughing up blood", "Symptoms lasting > 2 weeks"],
            "hi": ["3 दिन से अधिक 101°F से अधिक बुखार", "सांस लेने में कठिनाई", "सीने में दर्द",
                   "खून वाली खांसी", "2 सप्ताह से अधिक लक्षण"]
        },
        "needs_surgery": False
    },
    "diarrhea": {
        "en": ["diarrhea", "loose motion", "dast", "pakhala", "stomach upset"],
        "hi": "दस्त",
        "description": {
            "en": "Diarrhea is loose, watery stools occurring frequently. It's usually caused by infections or food issues.",
            "hi": "दस्त में बार-बार पतला मल आता है। यह आमतौर पर संक्रमण या खाने की समस्या के कारण होता है।"
        },
        "possible_causes": {
            "en": ["Viral gastroenteritis (stomach flu)", "Food poisoning", "Bacterial infection",
                   "Medication side effects (esp. antibiotics)", "Irritable bowel syndrome (IBS)",
                   "Traveler's diarrhea (E. coli)", "Lactose intolerance"],
            "hi": ["वायरल गैस्ट्रोएंटेराइटिस", "फूड पॉइजनिंग", "जीवाणु संक्रमण",
                   "दवा के दुष्प्रभाव (खासकर एंटीबायोटिक)", "इरिटेबल बाउल सिंड्रोम (IBS)",
                   "यात्री दस्त (ई. कोलाई)", "लैक्टोज असहिष्णुता"]
        },
        "home_remedies": {
            "en": ["ORS (Oral Rehydration Solution) frequently - 1 packet in 1 L water", "Eat BRAT diet (Banana, Rice, Apple, Toast)",
                   "Avoid dairy, spicy, oily food", "Stay well hydrated", "Probiotic yogurt (curd) helps",
                   "Avoid caffeine and alcohol"],
            "hi": ["ORS (ओरल रिहाइड्रेशन सॉल्यूशन) बार-बार पिएं - 1 पैकेट 1 लीटर पानी में", "BRAT आहार लें (केला, चावल, सेब, टोस्ट)",
                   "दूध, मसालेदार, तेल वाले खाने से बचें", "पर्याप्त पानी पिएं", "प्रोबायोटिक दही फायदेमंद",
                   "कैफीन और शराब से बचें"]
        },
        "medicines": [
            {"name": "ORS (Oral Rehydration Salts)", "dosage": "1 packet in 1 liter water, sip frequently", "type": "powder", "line": "first", "source": "WHO Essential Medicines; UNICEF"},
            {"name": "Zinc tablets (reduces duration)", "dosage": "20 mg daily for 14 days", "type": "tablet", "line": "first", "source": "WHO; ICMR India STW"},
            {"name": "Metronidazole (400mg - for amoebic infection)", "dosage": "400 mg three times daily - 5 days", "type": "tablet", "line": "second", "source": "WHO; ICMR India STW"},
            {"name": "Loperamide (for symptom relief - NOT for bloody diarrhea)", "dosage": "2 mg after each loose stool (max 8 mg/day)", "type": "capsule", "line": "second", "source": "WHO; ICMR India STW"},
            {"name": "Probiotics (Lactobacillus)", "dosage": "as directed on pack", "type": "capsule/powder", "line": "supplement", "source": "Cochrane Review"},
        ],
        "red_flags": {
            "en": ["Blood in stool (dysentery)", "High fever (>101°F)", "Severe abdominal pain",
                   "Signs of dehydration (dry mouth, no urine for 8h, dizziness)", "Diarrhea lasting > 1 week"],
            "hi": ["मल में खून (पेचिश)", "तेज बुखार (101°F से अधिक)", "तीव्र पेट दर्द",
                   "निर्जलीकरण के लक्षण (सूखा मुंह, 8 घंटे पेशाब न होना, चक्कर)", "1 सप्ताह से अधिक दस्त"]
        },
        "needs_surgery": False
    },
    "high_bp": {
        "en": ["high bp", "high blood pressure", "hypertension", "bp high", "blood pressure"],
        "hi": "उच्च रक्तचाप",
        "description": {
            "en": "High blood pressure is when blood flows through arteries at higher than normal pressure. Often has no symptoms.",
            "hi": "उच्च रक्तचाप तब होता है जब रक्त सामान्य से अधिक दबाव पर धमनियों में बहता है। अक्सर कोई लक्षण नहीं होते।"
        },
        "possible_causes": {
            "en": ["Genetics / Family history", "Obesity", "High salt intake", "Sedentary lifestyle",
                   "Stress", "Smoking / Alcohol", "Kidney disease", "Thyroid disorders"],
            "hi": ["आनुवंशिकता / पारिवारिक इतिहास", "मोटापा", "अधिक नमक खाना", "गतिहीन जीवनशैली",
                   "तनाव", "धूम्रपान / शराब", "गुर्दे की बीमारी", "थायराइड विकार"]
        },
        "home_remedies": {
            "en": ["Reduce salt intake (< 5g daily)", "Exercise 30 min daily (brisk walking)", "Maintain healthy weight",
                   "Reduce stress (meditation, yoga)", "Quit smoking", "Limit alcohol (max 1-2 drinks/day)",
                   "DASH diet (fruits, vegetables, whole grains, low-fat dairy)", "Monitor BP daily at home"],
            "hi": ["नमक कम खाएं (5g से कम रोज)", "रोज 30 मिनट व्यायाम करें (तेज चलना)", "स्वस्थ वजन रखें",
                   "तनाव कम करें (ध्यान, योग)", "धूम्रपान छोड़ें", "शराब सीमित करें (अधिकतम 1-2 पेय/दिन)",
                   "DASH आहार (फल, सब्जियां, साबुत अनाज, कम वसा वाला दूध)", "रोज घर पर BP जांचें"]
        },
        "medicines": [
            {"name": "Amlodipine (CCB)", "dosage": "5-10 mg once daily", "type": "tablet", "line": "first", "source": "WHO; JNC 8; ACC/AHA Guidelines"},
            {"name": "Telmisartan (ARB)", "dosage": "40-80 mg once daily", "type": "tablet", "line": "first", "source": "WHO; ACC/AHA"},
            {"name": "Metoprolol (Beta Blocker)", "dosage": "25-100 mg once or twice daily", "type": "tablet", "line": "first", "source": "WHO; ICMR India STW"},
            {"name": "Hydrochlorothiazide (Diuretic)", "dosage": "12.5-25 mg once daily", "type": "tablet", "line": "first", "source": "JNC 8; WHO"},
            {"name": "Losartan (ARB)", "dosage": "25-100 mg once or twice daily", "type": "tablet", "line": "first", "source": "WHO Essential Medicines"},
        ],
        "red_flags": {
            "en": ["BP > 180/120 (Hypertensive emergency - call 911)", "With chest pain, severe headache, vision changes, shortness of breath"],
            "hi": ["BP > 180/120 (उच्च रक्तचाप आपातकाल - तुरंत 108 पर कॉल करें)", "सीने में दर्द, तेज सिरदर्द, दृष्टि बदलना, सांस फूलना"]
        },
        "needs_surgery": False
    },
    "appendicitis": {
        "en": ["appendix pain", "appendicitis", "right lower abdomen pain", "naak ke niche dard"],
        "hi": "एपेंडिसाइटिस",
        "description": {
            "en": "Appendicitis is inflammation of the appendix, a small pouch attached to the large intestine. Needs urgent medical attention.",
            "hi": "एपेंडिसाइटिस एपेंडिक्स की सूजन है, जो बड़ी आंत से जुड़ी एक छोटी थैली है। तुरंत चिकित्सा की आवश्यकता है।"
        },
        "possible_causes": {
            "en": ["Blockage of appendix opening", "Infection", "Fecal mass", "Enlarged lymph nodes"],
            "hi": ["एपेंडिक्स के खुलने का अवरोध", "संक्रमण", "मलीय द्रव्यमान", "बढ़े हुए लिम्फ नोड्स"]
        },
        "home_remedies": {
            "en": ["DO NOT eat or drink", "DO NOT take laxatives or painkillers (masks symptoms)",
                   "Seek emergency medical care immediately"],
            "hi": ["कुछ न खाएं-पिएं", "जुलाब या दर्द निवारक न लें (लक्षण छिप जाते हैं)",
                   "तुरंत आपातकालीन चिकित्सा देखभाल लें"]
        },
        "medicines": [
            {"name": "IV Antibiotics (Ceftriaxone + Metronidazole)", "dosage": "IV as prescribed by surgeon", "type": "injection", "line": "pre-surgery", "source": "WSES Guidelines; ICMR India STW"},
        ],
        "red_flags": {
            "en": ["Pain migrating to lower right abdomen", "Nausea/vomiting", "Fever", "Loss of appetite",
                   "Pain worsening with movement/coughing"],
            "hi": ["दर्द निचले दाएं पेट में जाना", "मतली/उल्टी", "बुखार", "भूख न लगना",
                   "हिलने/खांसने पर दर्द बढ़ना"]
        },
        "needs_surgery": True,
        "surgery_detail": {
            "en": "Appendectomy (removal of appendix). Laparoscopic preferred - faster recovery (1-2 weeks). Source: WSES Guidelines for Acute Appendicitis",
            "hi": "एपेंडेक्टॉमी (एपेंडिक्स निकालना)। लेप्रोस्कोपिक बेहतर - तेज रिकवरी (1-2 सप्ताह)।"
        }
    },
    "kidney_stone": {
        "en": ["kidney stone", "stone", "pathri", "gurda pathri", "urine pain"],
        "hi": "गुर्दे की पथरी",
        "description": {
            "en": "Kidney stones are hard mineral and salt deposits that form inside the kidneys.",
            "hi": "गुर्दे की पथरी कठोर खनिज और नमक जमा होते हैं जो गुर्दे के अंदर बनते हैं।"
        },
        "possible_causes": {
            "en": ["Dehydration / Low water intake", "Diet high in salt/oxalate (spinach, nuts, chocolate)",
                   "Obesity", "Family history", "Certain medical conditions (gout, UTI)"],
            "hi": ["निर्जलीकरण / कम पानी पीना", "अधिक नमक/ऑक्सलेट वाला आहार (पालक, मेवे, चॉकलेट)",
                   "मोटापा", "पारिवारिक इतिहास", "कुछ चिकित्सीय स्थितियां (गठिया, UTI)"]
        },
        "home_remedies": {
            "en": ["Drink 8-10 glasses of water daily (most important)", "Limit salt intake",
                   "Reduce oxalate-rich foods (spinach, rhubarb, nuts, chocolate)",
                   "Lemon water (citrate helps prevent stones)", "Avoid excess animal protein"],
            "hi": ["रोज 8-10 गिलास पानी पिएं (सबसे ज़रूरी)", "नमक सीमित करें",
                   "ऑक्सलेट वाले खाद्य पदार्थ कम करें (पालक, रबर्ब, मेवे, चॉकलेट)",
                   "नींबू पानी (साइट्रेट पथरी रोकने में मदद करता है)", "अधिक पशु प्रोटीन से बचें"]
        },
        "medicines": [
            {"name": "Diclofenac Sodium (for acute pain)", "dosage": "75 mg IM or 50 mg oral as needed", "type": "injection/tablet", "line": "first", "source": "EAU Guidelines; ICMR India STW"},
            {"name": "Tamsulosin (for stone passage - alpha blocker)", "dosage": "0.4 mg once daily, up to 4 weeks", "type": "tablet", "line": "first", "source": "EAU Guidelines; AUA Guidelines"},
            {"name": "Paracetamol (for mild pain)", "dosage": "500-650 mg every 6 hours", "type": "tablet", "line": "first", "source": "WHO"},
        ],
        "red_flags": {
            "en": ["Severe pain with vomiting", "Blood in urine", "Fever with chills (kidney infection)",
                   "Inability to pass urine (obstruction)"],
            "hi": ["उल्टी के साथ तेज दर्द", "पेशाब में खून", "बुखार के साथ ठंड लगना (गुर्दे में संक्रमण)",
                   "पेशाब न कर पाना (अवरोध)"]
        },
        "needs_surgery": True,
        "surgery_detail": {
            "en": "Options: ESWL (shock wave - non-invasive for <2cm stones), Ureteroscopy (RIRS), PCNL (for >2cm). Small stones (<5mm) can pass naturally. Source: EAU/AUA Guidelines",
            "hi": "विकल्प: ESWL (शॉक वेव - 2cm से छोटी पथरी के लिए), यूरेटेरोस्कोपी (RIRS), PCNL (2cm से बड़ी के लिए)। छोटी पथरी (<5mm) प्राकृतिक रूप से निकल सकती है।"
        }
    },
    "diabetes": {
        "en": ["diabetes", "sugar", "diabetic", "blood sugar", "shugar"],
        "hi": "मधुमेह / शुगर",
        "description": {
            "en": "Diabetes is a chronic condition where blood sugar levels are too high due to insulin problems.",
            "hi": "मधुमेह एक पुरानी स्थिति है जहां इंसुलिन की समस्या के कारण रक्त शर्करा का स्तर बहुत अधिक हो जाता है।"
        },
        "possible_causes": {
            "en": ["Type 1: Autoimmune", "Type 2: Insulin resistance (obesity, lifestyle, genetics)",
                   "Gestational diabetes (pregnancy)", "Prediabetes"],
            "hi": ["टाइप 1: ऑटोइम्यून", "टाइप 2: इंसुलिन प्रतिरोध (मोटापा, जीवनशैली, आनुवंशिकता)",
                   "गर्भकालीन मधुमेह (गर्भावस्था)", "प्रीडायबिटीज"]
        },
        "home_remedies": {
            "en": ["Low sugar, low carb diet", "Regular exercise 30-45 min daily", "Monitor blood sugar regularly",
                   "Maintain healthy weight", "Include fenugreek (methi), bitter gourd (karela)",
                   "Eat high fiber foods (oats, whole grains, legumes)"],
            "hi": ["कम चीनी, कम कार्ब्स वाला आहार", "रोज 30-45 मिनट व्यायाम करें", "नियमित रक्त शर्करा जांचें",
                   "स्वस्थ वजन रखें", "मेथी, करेला आहार में शामिल करें",
                   "उच्च फाइबर वाले खाद्य पदार्थ खाएं (ओट्स, साबुत अनाज, दालें)"]
        },
        "medicines": [
            {"name": "Metformin", "dosage": "500 mg once/twice daily with meals (max 2000 mg/day)", "type": "tablet", "line": "first", "source": "ADA/EASD Guidelines; WHO Essential Medicines"},
            {"name": "Glimepiride (Sulfonylurea)", "dosage": "1-4 mg once daily before breakfast", "type": "tablet", "line": "second", "source": "ADA; ICMR India STW"},
            {"name": "Dapagliflozin (SGLT2 inhibitor)", "dosage": "5-10 mg once daily", "type": "tablet", "line": "second", "source": "ADA/EASD; ESC Guidelines"},
            {"name": "Insulin (various types)", "dosage": "as prescribed by endocrinologist", "type": "injection", "line": "third", "source": "ADA/EASD; WHO"},
        ],
        "red_flags": {
            "en": ["Very high blood sugar (>400 mg/dL)", "DKA symptoms (nausea, vomiting, deep breathing, fruity breath)",
                   "Frequent infections / slow healing wounds", "Sudden vision changes"],
            "hi": ["बहुत अधिक रक्त शर्करा (400 mg/dL से अधिक)", "DKA के लक्षण (मतली, उल्टी, गहरी सांस, फल जैसी गंध)",
                   "बार-बार संक्रमण / धीमी गति से घाव भरना", "अचानक दृष्टि में बदलाव"]
        },
        "needs_surgery": True,
        "surgery_detail": {
            "en": "Can lead to: diabetic foot ulcers (debridement/amputation), cataract surgery, bariatric surgery. Glucose control essential before any surgery. Source: ADA Standards of Care",
            "hi": "डायबिटिक फुट अल्सर, मोतियाबिंद सर्जरी, बेरिएट्रिक सर्जरी की आवश्यकता हो सकती है। सर्जरी से पहले ग्लूकोज नियंत्रण आवश्यक।"
        }
    },
    "depression": {
        "en": ["depression", "depressed", "udaas", "sad", "hopeless", "mental"],
        "hi": "अवसाद",
        "description": {
            "en": "Depression is a mood disorder causing persistent sadness and loss of interest in activities.",
            "hi": "अवसाद एक मूड विकार है जो लगातार उदासी और गतिविधियों में रुचि की कमी का कारण बनता है।"
        },
        "possible_causes": {
            "en": ["Chemical imbalance in brain", "Genetics", "Traumatic life events", "Chronic stress",
                   "Hormonal changes", "Chronic illness", "Medication side effects"],
            "hi": ["मस्तिष्क में रासायनिक असंतुलन", "आनुवंशिकता", "दर्दनाक जीवन घटनाएं", "लगातार तनाव",
                   "हार्मोनल बदलाव", "पुरानी बीमारी", "दवा के दुष्प्रभाव"]
        },
        "home_remedies": {
            "en": ["Talk to someone you trust", "Regular exercise (even 15 min walking helps)",
                   "Maintain daily routine", "Practice mindfulness/meditation",
                   "Set small achievable goals", "Stay connected with family/friends",
                   "Avoid alcohol and drugs"],
            "hi": ["किसी भरोसेमंद व्यक्ति से बात करें", "नियमित व्यायाम (15 मिनट चलना भी मदद करता है)",
                   "दैनिक दिनचर्या बनाए रखें", "ध्यान/माइंडफुलनेस का अभ्यास करें",
                   "छोटे लक्ष्य निर्धारित करें", "परिवार/दोस्तों के संपर्क में रहें",
                   "शराब और नशीली दवाओं से बचें"]
        },
        "medicines": [
            {"name": "Fluoxetine (SSRI)", "dosage": "20-80 mg once daily - start 20 mg", "type": "capsule", "line": "first", "source": "WHO Essential Medicines; APA Guidelines"},
            {"name": "Sertraline (SSRI)", "dosage": "50-200 mg once daily - start 50 mg", "type": "tablet", "line": "first", "source": "WHO Essential Medicines; APA Guidelines"},
            {"name": "Escitalopram (SSRI)", "dosage": "10-20 mg once daily", "type": "tablet", "line": "first", "source": "APA Guidelines; NICE"},
            {"name": "Amitriptyline (TCA - also for sleep)", "dosage": "25-75 mg at bedtime", "type": "tablet", "line": "second", "source": "WHO; ICMR India STW"},
        ],
        "red_flags": {
            "en": ["Suicidal thoughts or self-harm", "Not eating or drinking for days",
                   "Complete withdrawal from all activities", "Hallucinations or delusions",
                   "If you feel like hurting yourself - call 988 (India: 9152987821)"],
            "hi": ["आत्महत्या के विचार या स्वयं को नुकसान", "दिनों तक कुछ न खाना-पीना",
                   "सभी गतिविधियों से पूरी तरह अलग होना", "मतिभ्रम या भ्रम",
                   "यदि खुद को नुकसान पहुंचाने का मन करे - 988 पर कॉल करें (भारत: 9152987821)"]
        },
        "needs_surgery": False
    },
    "anxiety": {
        "en": ["anxiety", "anxious", "tension", "stress", "ghabrahat", "worried",
               "nervous", "panic", "overthinking", "chinta", "tanav", "gabrahat"],
        "hi": "चिंता / तनाव",
        "description": {
            "en": "Anxiety is a feeling of worry, nervousness or unease about something with an uncertain outcome.",
            "hi": "चिंता एक ऐसी भावना है जिसमें किसी अनिश्चित परिणाम को लेकर घबराहट या बेचैनी होती है।"
        },
        "possible_causes": {
            "en": ["Stressful life events", "Genetics", "Brain chemistry imbalance",
                   "Trauma", "Chronic health conditions", "Substance use",
                   "Personality type", "Hormonal changes"],
            "hi": ["तनावपूर्ण जीवन की घटनाएं", "आनुवंशिकता", "मस्तिष्क रसायन असंतुलन",
                   "आघात", "पुरानी स्वास्थ्य स्थितियां", "नशीले पदार्थों का उपयोग",
                   "व्यक्तित्व प्रकार", "हार्मोनल बदलाव"]
        },
        "home_remedies": {
            "en": ["Deep breathing exercises (4-7-8 technique)", "Regular exercise (walking, yoga)",
                   "Reduce caffeine and sugar intake", "Get 7-8 hours of sleep",
                   "Talk to a trusted friend or family member",
                   "Practice mindfulness and meditation",
                   "Write down your worries in a journal",
                   "Take breaks from screens and social media"],
            "hi": ["गहरी सांस लेने का व्यायाम (4-7-8 तकनीक)", "नियमित व्यायाम (चलना, योग)",
                   "कैफीन और चीनी कम करें", "7-8 घंटे की नींद लें",
                   "किसी भरोसेमंद दोस्त या परिवार से बात करें",
                   "ध्यान और माइंडफुलनेस का अभ्यास करें",
                   "अपनी चिंताएं एक डायरी में लिखें",
                   "स्क्रीन और सोशल मीडिया से ब्रेक लें"]
        },
        "medicines": [
            {"name": "Buspirone (Anxiolytic)", "dosage": "5-10 mg twice daily - start 5 mg", "type": "tablet", "line": "first", "source": "WHO; APA Guidelines"},
            {"name": "Escitalopram (SSRI - for anxiety)", "dosage": "10-20 mg once daily - start 10 mg", "type": "tablet", "line": "first", "source": "APA Guidelines; NICE"},
            {"name": "Propranolol (for performance anxiety)", "dosage": "10-40 mg before triggering event", "type": "tablet", "line": "second", "source": "NICE Guidelines"},
        ],
        "red_flags": {
            "en": ["Panic attacks (racing heart, difficulty breathing)", "Constant worry interfering with daily life",
                   "Avoiding social situations completely", "Suicidal thoughts",
                   "If you feel overwhelmed - call a helpline: 988 (India: 9152987821)"],
            "hi": ["पैनिक अटैक (तेज़ दिल की धड़कन, सांस लेने में कठिनाई)", "लगातार चिंता जो दैनिक जीवन में बाधा डाले",
                   "सामाजिक स्थितियों से पूरी तरह बचना", "आत्महत्या के विचार",
                   "यदि अभिभूत महसूस करें - हेल्पलाइन: 988 (भारत: 9152987821)"]
        },
        "needs_surgery": False
    }
}

SURGERY_INFO = {
    "appendectomy": {
        "en": "Appendectomy - Removal of appendix",
        "hi": "एपेंडेक्टॉमी - एपेंडिक्स निकालना",
        "details": {
            "en": "Laparoscopic or open. Recovery 1-2 weeks. Gold standard for acute appendicitis. Source: WSES Guidelines",
            "hi": "लेप्रोस्कोपिक या ओपन। रिकवरी 1-2 सप्ताह। तीव्र एपेंडिसाइटिस के लिए गोल्ड स्टैंडर्ड।"
        }
    },
    "cholecystectomy": {
        "en": "Cholecystectomy - Gallbladder removal",
        "hi": "कोलेसिस्टेक्टॉमी - पित्ताशय निकालना",
        "details": {
            "en": "Laparoscopic is standard. For gallstones, polyps. Recovery 1-2 weeks. Source: SAGES Guidelines",
            "hi": "लेप्रोस्कोपिक मानक है। पथरी, पॉलिप्स के लिए। रिकवरी 1-2 सप्ताह।"
        }
    },
    "hernia_repair": {
        "en": "Hernia Repair - Mesh or suture",
        "hi": "हर्निया मरम्मत - जाल या टांका",
        "details": {
            "en": "Open or laparoscopic. Mesh reduces recurrence. Recovery 2-4 weeks. Source: EHS Guidelines",
            "hi": "ओपन या लेप्रोस्कोपिक। जाल से पुनरावृत्ति कम होती है। रिकवरी 2-4 सप्ताह।"
        }
    },
    "cabg": {
        "en": "CABG (Coronary Artery Bypass Grafting)",
        "hi": "CABG - हृदय बाइपास सर्जरी",
        "details": {
            "en": "Open heart surgery for blocked arteries. Recovery 6-12 weeks. Cardiac rehab required. Source: ACC/AHA Guidelines",
            "hi": "ओपन हार्ट सर्जरी। बंद धमनियों के लिए। रिकवरी 6-12 सप्ताह। कार्डियक रिहैब आवश्यक।"
        }
    },
    "cataract": {
        "en": "Cataract Surgery - Lens replacement",
        "hi": "मोतियाबिंद सर्जरी",
        "details": {
            "en": "Phacoemulsification - daycare procedure. Quick recovery. Source: AAO Guidelines",
            "hi": "फेक्टोइमल्सीफिकेशन - डेकेयर प्रक्रिया। तेज रिकवरी।"
        }
    },
    "knee_replacement": {
        "en": "Knee Replacement (Total Knee Arthroplasty)",
        "hi": "घुटना बदलना (TKA)",
        "details": {
            "en": "For severe arthritis - replaces damaged joint with implant. Recovery 4-6 months. Source: AAOS Guidelines",
            "hi": "गंभीर गठिया के लिए। रिकवरी 4-6 महीने।"
        }
    },
    "spinal_fusion": {
        "en": "Spinal Fusion - Joining vertebrae",
        "hi": "स्पाइनल फ्यूजन",
        "details": {
            "en": "For herniated disc, stenosis, scoliosis. Recovery 3-6 months. Physical therapy required. Source: NASS Guidelines",
            "hi": "हर्नियेटेड डिस्क, स्टेनोसिस के लिए। रिकवरी 3-6 महीने। फिजिकल थेरेपी आवश्यक।"
        }
    },
    "laparoscopic": {
        "en": "Laparoscopic Surgery - Keyhole surgery",
        "hi": "लेप्रोस्कोपिक सर्जरी",
        "details": {
            "en": "Small incisions, camera-guided. Used for appendix, gallbladder, hernia. Less pain, faster recovery. Source: SAGES/EAES Guidelines",
            "hi": "छोटे चीरे, कैमरा-निर्देशित। कम दर्द, तेज रिकवरी।"
        }
    },
    "lipoma_removal": {
        "en": "Lipoma Removal - Benign tumor excision",
        "hi": "लिपोमा निकालना",
        "details": {
            "en": "Simple excision under local anesthesia. Daycare. Recovery 1 week.",
            "hi": "लोकल एनेस्थीसिया में सरल उच्छेदन। डेकेयर। रिकवरी 1 सप्ताह।"
        }
    }
}

MEDICINES_DB = {
    "paracetamol": {
        "generic": "Paracetamol / Acetaminophen",
        "brands": ["Crocin", "Calpol", "Tylenol", "Pacimol", "Fevastin", "Sumo"],
        "class": "Para-aminophenol derivative (analgesic-antipyretic)",
        "uses": {
            "en": ["Fever reduction", "Mild to moderate pain (headache, body ache, toothache, period pain)"],
            "hi": ["बुखार कम करना", "हल्के से मध्यम दर्द में राहत (सिरदर्द, बदन दर्द, दांत दर्द, पीरियड दर्द)"]
        },
        "dosage": {
            "en": "Adults: 500-1000 mg every 4-6 hours (max 4000 mg/day). Children: 15 mg/kg every 6 hours (max 60 mg/kg/day).",
            "hi": "वयस्क: 500-1000 mg हर 4-6 घंटे (अधिकतम 4000 mg/दिन)। बच्चे: 15 mg/kg हर 6 घंटे।"
        },
        "side_effects": {
            "en": ["Rare at therapeutic doses", "Liver damage with overdose (>4000 mg/day or chronic high doses)", "Skin rash (rare)"],
            "hi": ["चिकित्सीय खुराक पर दुर्लभ", "अधिक मात्रा में जिगर की क्षति (>4000 mg/दिन)", "त्वचा पर दाने (दुर्लभ)"]
        },
        "contraindications": {
            "en": ["Severe liver disease", "Alcoholism (chronic heavy drinkers at risk of liver damage)"],
            "hi": ["गंभीर जिगर की बीमारी", "शराब की लत (पुरानी शराब पीने वालों में जिगर क्षति का खतरा)"]
        },
        "sources": ["WHO Essential Medicines List", "ICMR India Standard Treatment Workflows", "Mayo Clinic"]
    },
    "ibuprofen": {
        "generic": "Ibuprofen",
        "brands": ["Brufen", "Ibubid", "Advil", "Motrin", "Emflam"],
        "class": "NSAID (Non-steroidal anti-inflammatory drug)",
        "uses": {
            "en": ["Pain relief (headache, muscle pain, period pain)", "Fever reduction",
                   "Anti-inflammatory (arthritis, sprains, dental pain)",
                   "More effective than paracetamol for tension-type headache (DFG/UpToDate)"],
            "hi": ["दर्द राहत (सिरदर्द, मांसपेशियों का दर्द, मासिक धर्म दर्द)", "बुखार कम करना",
                   "सूजनरोधी (गठिया, मोच, दांत का दर्द)",
                   "तनाव सिरदर्द में पैरासिटामोल से अधिक प्रभावी (DFG/UpToDate)"]
        },
        "dosage": {
            "en": "Adults: 200-400 mg every 6-8 hours with food (max 1200 mg/day OTC, up to 3200 mg/day prescription).",
            "hi": "वयस्क: 200-400 mg हर 6-8 घंटे भोजन के साथ (अधिकतम 1200 mg/दिन OTC, प्रिस्क्रिप्शन में 3200 mg/दिन तक)।"
        },
        "side_effects": {
            "en": ["Stomach upset/heartburn", "Gastric ulcers with long-term use", "Increased bleeding risk",
                   "Kidney impairment (long-term)", "Dizziness", "Fluid retention"],
            "hi": ["पेट की गड़बड़ी/जलन", "लंबे उपयोग से पेट के अल्सर", "रक्तस्राव का खतरा बढ़ना",
                   "गुर्दे पर प्रभाव (लंबे समय में)", "चक्कर", "तरल पदार्थ जमा होना"]
        },
        "contraindications": {
            "en": ["Active stomach ulcer", "Severe kidney disease", "Third trimester of pregnancy",
                   "Aspirin allergy (cross-sensitivity)", "Severe heart disease", "Dengue fever (bleeding risk)"],
            "hi": ["सक्रिय पेट का अल्सर", "गंभीर गुर्दे की बीमारी", "गर्भावस्था की तीसरी तिमाही",
                   "एस्पिरिन से एलर्जी", "गंभीर हृदय रोग", "डेंगू बुखार (रक्तस्राव का खतरा)"]
        },
        "sources": ["WHO Essential Medicines List", "Mayo Clinic", "UpToDate", "NICE Guidelines",
                    "Scientific Reports 2023 - Paracetamol vs Ibuprofen for TTH"]
    },
    "amoxicillin": {
        "generic": "Amoxicillin",
        "brands": ["Amoxil", "Mox", "Novamox", "Klenok-D"],
        "class": "Penicillin antibiotic",
        "uses": {
            "en": ["Bacterial infections: respiratory (sinusitis, otitis media, pneumonia)",
                   "UTI, throat infections, dental infections"],
            "hi": ["जीवाणु संक्रमण: श्वसन (साइनसाइटिस, कान संक्रमण, निमोनिया)",
                   "मूत्र मार्ग संक्रमण, गले के संक्रमण, दांतों के संक्रमण"]
        },
        "dosage": {
            "en": "Adults: 250-500 mg every 8 hours or 875 mg every 12 hours. Course: 5-7 days (uncomplicated) to 10-14 days.",
            "hi": "वयस्क: 250-500 mg हर 8 घंटे या 875 mg हर 12 घंटे। कोर्स: 5-7 दिन से 10-14 दिन।"
        },
        "side_effects": {
            "en": ["Diarrhea", "Nausea", "Skin rash", "Allergic reactions (urticaria, anaphylaxis - rare but serious)"],
            "hi": ["दस्त", "मतली", "त्वचा पर दाने", "एलर्जी प्रतिक्रिया (पित्ती, एनाफिलेक्सिस - दुर्लभ लेकिन गंभीर)"]
        },
        "contraindications": {
            "en": ["Penicillin allergy (can cause anaphylaxis - DO NOT take if allergic)"],
            "hi": ["पेनिसिलिन से एलर्जी (एनाफिलेक्सिस हो सकता है - एलर्जी होने पर न लें)"]
        },
        "sources": ["WHO Essential Medicines List", "ICMR India STW", "Sanford Guide"]
    },
    "metformin": {
        "generic": "Metformin",
        "brands": ["Glucophage", "Glyciphage", "Odimet", "Bigomet"],
        "class": "Biguanide (anti-diabetic)",
        "uses": {
            "en": ["Type 2 diabetes (first-line therapy per ADA/EASD)", "PCOS (off-label)", "Prediabetes"],
            "hi": ["टाइप 2 मधुमेह (ADA/EASD के अनुसार प्रथम-पंक्ति)", "PCOS (ऑफ-लेबल)", "प्रीडायबिटीज"]
        },
        "dosage": {
            "en": "Start 500 mg once/twice daily with meals. Titrate slowly. Max: 2000-2550 mg/day in divided doses.",
            "hi": "शुरुआत 500 mg दिन में एक/दो बार भोजन के साथ। धीरे-धीरे बढ़ाएं। अधिकतम: 2000-2550 mg/दिन।"
        },
        "side_effects": {
            "en": ["Nausea/diarrhea (common - start low, go slow)", "Metallic taste",
                   "Vitamin B12 deficiency (long-term - monitor)", "Lactic acidosis (rare)"],
            "hi": ["मतली/दस्त (आम - कम खुराक से शुरू करें)", "धातु जैसा स्वाद",
                   "विटामिन B12 की कमी (लंबे समय में - जांच कराएं)", "लैक्टिक एसिडोसिस (दुर्लभ)"]
        },
        "contraindications": {
            "en": ["Severe kidney disease (eGFR <30)", "Severe liver disease", "Alcoholism", "Acute illness with dehydration"],
            "hi": ["गंभीर गुर्दे की बीमारी (eGFR <30)", "गंभीर जिगर की बीमारी", "शराब की लत", "निर्जलीकरण के साथ तीव्र बीमारी"]
        },
        "sources": ["ADA Standards of Care", "EASD Guidelines", "WHO Essential Medicines List"]
    },
    "amlodipine": {
        "generic": "Amlodipine",
        "brands": ["Amlopin", "Amlokind", "Norvasc", "Stamlo"],
        "class": "CCB (Calcium Channel Blocker)",
        "uses": {
            "en": ["Hypertension (first-line)", "Coronary artery disease / Angina"],
            "hi": ["उच्च रक्तचाप (प्रथम-पंक्ति)", "कोरोनरी धमनी रोग / एनजाइना"]
        },
        "dosage": {
            "en": "2.5-10 mg once daily. Start 5 mg, adjust based on response.",
            "hi": "2.5-10 mg दिन में एक बार। 5 mg से शुरू करें, प्रतिक्रिया के अनुसार समायोजित करें।"
        },
        "side_effects": {
            "en": ["Ankle swelling (edema - common)", "Dizziness", "Headache", "Flushing", "Palpitations"],
            "hi": ["टखने में सूजन (आम)", "चक्कर", "सिरदर्द", "चेहरे का लाल होना", "धड़कन"]
        },
        "contraindications": {
            "en": ["Severe hypotension", "Aortic stenosis", "Cardiogenic shock"],
            "hi": ["गंभीर निम्न रक्तचाप", "महाधमनी स्टेनोसिस", "कार्डियोजेनिक शॉक"]
        },
        "sources": ["JNC 8 Guidelines", "ACC/AHA Hypertension Guidelines", "WHO Essential Medicines List"]
    },
    "pantoprazole": {
        "generic": "Pantoprazole",
        "brands": ["Pantocid", "Pantodac", "Pan", "Protonix"],
        "class": "PPI (Proton Pump Inhibitor)",
        "uses": {
            "en": ["GERD / Acid reflux", "Peptic ulcer disease", "H. pylori eradication (combination)", "Stress ulcer prophylaxis"],
            "hi": ["GERD / एसिड रिफ्लक्स", "पेप्टिक अल्सर", "H. pylori उन्मूलन (संयोजन)", "स्ट्रेस अल्सर प्रोफिलैक्सिस"]
        },
        "dosage": {
            "en": "40 mg once daily before breakfast. Severe: 40 mg twice daily. Max 80 mg/day.",
            "hi": "40 mg दिन में एक बार नाश्ते से पहले। गंभीर: 40 mg दिन में दो बार। अधिकतम 80 mg/दिन।"
        },
        "side_effects": {
            "en": ["Headache", "Diarrhea/constipation", "Nausea",
                   "Long-term: Vitamin B12 deficiency, increased fracture risk, C. diff infection"],
            "hi": ["सिरदर्द", "दस्त/कब्ज", "मतली",
                   "लंबे समय में: विटामिन B12 की कमी, फ्रैक्चर का खतरा, C. diff संक्रमण"]
        },
        "contraindications": {
            "en": ["Severe liver disease", "PPI allergy", "Long-term use without medical need"],
            "hi": ["गंभीर जिगर की बीमारी", "PPI से एलर्जी"]
        },
        "sources": ["ACG Guidelines for GERD", "ICMR India STW", "WHO Essential Medicines List"]
    },
    "cetirizine": {
        "generic": "Cetirizine",
        "brands": ["Alerid", "Cetzine", "Zycet", "Zyrtec"],
        "class": "Second-generation antihistamine",
        "uses": {
            "en": ["Allergic rhinitis (hay fever)", "Urticaria (hives)", "Pruritus (itching)", "Common cold symptoms"],
            "hi": ["एलर्जिक राइनाइटिस", "पित्ती", "खुजली", "सामान्य सर्दी के लक्षण"]
        },
        "dosage": {
            "en": "Adults: 10 mg once daily (preferably at night due to drowsiness). Children (6-12): 5 mg daily.",
            "hi": "वयस्क: 10 mg दिन में एक बार (रात में लेना बेहतर)। बच्चे (6-12 वर्ष): 5 mg दैनिक।"
        },
        "side_effects": {
            "en": ["Mild drowsiness (less sedating than older antihistamines)", "Fatigue", "Dry mouth"],
            "hi": ["हल्का उनींदापन (पुरानी एंटीहिस्टामाइन से कम)", "थकान", "मुंह सूखना"]
        },
        "contraindications": {
            "en": ["Severe kidney disease (dose adjustment needed)", "Allergy to hydroxyzine or cetirizine"],
            "hi": ["गंभीर गुर्दे की बीमारी (खुराक समायोजन आवश्यक)", "हाइड्रॉक्सीज़ाइन या सेटीरिज़िन से एलर्जी"]
        },
        "sources": ["WHO Essential Medicines List", "ICMR India STW", "AAAAI Guidelines"]
    },
    "fluoxetine": {
        "generic": "Fluoxetine",
        "brands": ["Prozac", "Fludac", "Sarafem"],
        "class": "SSRI (Selective Serotonin Reuptake Inhibitor)",
        "uses": {
            "en": ["Depression", "OCD", "Bulimia nervosa", "Panic disorder", "Premenstrual dysphoric disorder"],
            "hi": ["अवसाद", "OCD", "बुलिमिया नर्वोसा", "पैनिक डिसऑर्डर", "प्रीमेंस्ट्रुअल डिस्फोरिक डिसऑर्डर"]
        },
        "dosage": {
            "en": "20-80 mg once daily. Start 20 mg in morning. Full effect in 4-6 weeks. Use 4-6 month minimum.",
            "hi": "20-80 mg दिन में एक बार। 20 mg सुबह से शुरू करें। पूरा प्रभाव 4-6 सप्ताह में। न्यूनतम 4-6 महीने उपयोग।"
        },
        "side_effects": {
            "en": ["Nausea (common initially)", "Insomnia", "Anxiety (initial - usually subsides)",
                   "Sexual dysfunction (common)", "Weight changes", "Discontinuation syndrome (with abrupt stop)"],
            "hi": ["मतली (शुरुआत में आम)", "अनिद्रा", "चिंता (शुरुआत में - आमतौर पर कम हो जाती है)",
                   "यौन रोग (आम)", "वजन में बदलाव", "अचानक बंद करने पर वापसी के लक्षण"]
        },
        "contraindications": {
            "en": ["MAO inhibitor use in last 14 days", "Bipolar disorder (can trigger mania without mood stabilizer)"],
            "hi": ["पिछले 14 दिनों में MAO इन्हिबिटर का उपयोग", "द्विध्रुवी विकार (मूड स्टेबलाइजर के बिना उन्माद शुरू कर सकता है)"]
        },
        "sources": ["APA Practice Guidelines", "WHO Essential Medicines List", "NICE Guidelines", "Lancet 2018"]
    }
}

DOCTOR_PROFILE = {
    "name": "Dr. Aarogya",
    "qualifications": {
        "en": "MBBS, MD (Internal Medicine), Fellowship in Surgery",
        "hi": "एमबीबीएस, एमडी (आंतरिक चिकित्सा), सर्जरी में फेलोशिप"
    },
    "experience": {
        "en": "AI and Made by Mohit Anand",
        "hi": "AI और मोहित आनंद द्वारा निर्मित"
    },
    "hospital": {
        "en": "Aarogya Multispecialty Hospital",
        "hi": "आरोग्य मल्टीस्पेशलिटी हॉस्पिटल"
    }
}

GREETINGS = {
    "en": [
        "Namaste! I'm Dr. Aarogya. Tell me your health concern.",
        "Hello! I'm Dr. Aarogya. What's troubling you?",
        "Hi! Dr. Aarogya here. Describe your symptoms."
    ],
    "hi": [
        "नमस्ते! मैं डॉ. आरोग्य हूं। अपनी समस्या बताएं।",
        "नमस्कार! मैं डॉ. आरोग्य। क्या परेशानी है?",
        "हैलो! डॉ. आरोग्य बोल रहा हूं। अपने लक्षण बताएं।"
    ]
}

EMERGENCY_KEYWORDS = {
    "en": ["emergency", "urgent", "accident", "severe pain", "heart attack", "stroke", "unconscious",
           "not breathing", "bleeding heavily", "poisoning", "trauma", "911"],
    "hi": ["आपातकाल", "एमरजेंसी", "दुर्घटना", "तेज दर्द", "हार्ट अटैक", "स्ट्रोक", "बेहोश",
           "सांस नहीं आ रही", "बहुत खून बह रहा", "जहर", "चोट"]
}
