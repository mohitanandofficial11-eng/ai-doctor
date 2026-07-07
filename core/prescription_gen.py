from datetime import datetime, timedelta


class PrescriptionGenerator:
    def __init__(self, patient_name="Patient", lang="en"):
        self.patient_name = patient_name
        self.lang = lang
        self.medicines = []
        self.advice = []
        self.investigations = []
        self.follow_up = ""
        self.date = datetime.now()

    def add_medicine(self, name, dosage, duration="", timing="", note=""):
        if isinstance(name, dict):
            self.medicines.append(name)
        else:
            self.medicines.append({
                "name": name,
                "dosage": dosage,
                "duration": duration,
                "timing": timing,
                "note": note
            })

    def add_advice(self, advice_text):
        self.advice.append(advice_text)

    def add_investigation(self, test_name):
        self.investigations.append(test_name)

    def set_follow_up(self, follow_up_text):
        self.follow_up = follow_up_text

    def generate(self):
        labels = {
            "header": ("Dr. Aarogya", "डॉ. आरोग्य"),
            "qualifications": ("MBBS, MD (Internal Medicine), FICS (Surgery)", "एमबीबीएस, एमडी (आंतरिक चिकित्सा), एफआईसीएस (सर्जरी)"),
            "hospital": ("Internet Hospital", "इंटरनेट हॉस्पिटल"),
            "reg_no": ("Reg. No: DEL-MC-2010-04256", "पंजीकरण संख्या: DEL-MC-2010-04256"),
            "prescription_title": ("PRESCRIPTION", "पर्चा"),
            "patient": ("Patient:", "मरीज:"),
            "date": ("Date:", "तारीख:"),
            "medicines_header": ("Prescribed Medicines:", "निर्धारित दवाएं:"),
            "advice_header": ("Advice & Precautions:", "सलाह और सावधानियां:"),
            "investigations_header": ("Investigations:", "जांचें:"),
            "follow_up_title": ("Follow Up:", "दोबारा मिलें:"),
            "footer_note": ("This prescription is AI-generated for informational purposes. Please consult a qualified doctor.",
                           "यह पर्चा AI द्वारा जानकारी के लिए बनाया गया है। कृपया योग्य डॉक्टर से सलाह लें।"),
            "medicine": ("Medicine", "दवा"),
            "dosage": ("Dosage", "मात्रा"),
            "duration": ("Duration", "अवधि"),
            "timing": ("Timing", "समय"),
            "note": ("Note", "नोट"),
            "advice_item": ("Advice", "सलाह"),
            "empty_state": ("No medicines prescribed yet.", "अभी कोई दवा निर्धारित नहीं की गई है।"),
            "no_investigations": ("No investigations suggested.", "कोई जांच सुझाई नहीं गई।"),
            "diagnosis": ("Diagnosis:", "निदान:"),
            "signature": ("Dr. Aarogya", "डॉ. आरोग्य"),
            "signature_line": ("Signature", "हस्ताक्षर"),
        }

        idx = 0 if self.lang == "en" else 1

        lines = []
        lines.append("=" * 60)
        lines.append(f"{labels['header'][idx]:^60}")
        lines.append(f"{labels['qualifications'][idx]:^60}")
        lines.append(f"{labels['hospital'][idx]:^60}")
        lines.append(f"{labels['reg_no'][idx]:^60}")
        lines.append("=" * 60)
        lines.append(f"{labels['prescription_title'][idx]:^60}")
        lines.append("-" * 60)
        lines.append(f"{labels['patient'][idx]} {self.patient_name}")
        lines.append(
            f"{labels['date'][idx]} {self.date.strftime('%d-%b-%Y, %H:%M')}")
        lines.append("-" * 60)

        if self.medicines:
            lines.append(f"\n{labels['medicines_header'][idx]}")
            lines.append(f"{'-'*20} {'-'*20} {'-'*10} {'-'*10}")
            lines.append(
                f"{labels['medicine'][idx]:<20} {labels['dosage'][idx]:<20} {labels['timing'][idx]:<10} {labels['note'][idx]}")
            lines.append(f"{'-'*20} {'-'*20} {'-'*10} {'-'*10}")
            for med in self.medicines:
                name = med.get("name", "")
                dosage = med.get("dosage", "")
                timing = med.get("timing", "")
                note = med.get("note", "")
                lines.append(f"{name:<20} {dosage:<20} {timing:<10} {note}")

        if self.advice:
            lines.append(f"\n{labels['advice_header'][idx]}")
            for i, adv in enumerate(self.advice, 1):
                lines.append(f"  {i}. {adv}")

        if self.investigations:
            lines.append(f"\n{labels['investigations_header'][idx]}")
            for inv in self.investigations:
                lines.append(f"  - {inv}")

        if self.follow_up:
            lines.append(
                f"\n{labels['follow_up_title'][idx]} {self.follow_up}")

        lines.append("-" * 60)
        lines.append(f"\n  {labels['signature'][idx]}")
        lines.append(f"  ({labels['signature_line'][idx]})")
        lines.append(f"\n{'_' * 60}")
        lines.append(f"{labels['footer_note'][idx]:^60}")

        return "\n".join(lines)

    def generate_markdown(self):
        idx = 0 if self.lang == "en" else 1
        labels = {
            "name": ("Dr. Aarogya", "डॉ. आरोग्य"),
            "qual": ("MBBS, MD, FICS (Surgery)", "एमबीबीएस, एमडी, एफआईसीएस (सर्जरी)"),
            "hosp": ("Internet Hospital", "इंटरनेट हॉस्पिटल"),
            "reg": ("Reg: DEL-MC-2010-04256", "पंजी: DEL-MC-2010-04256"),
            "rx_title": ("📋 PRESCRIPTION", "📋 पर्चा"),
            "patient": ("🧑‍⚕️ Patient:", "🧑‍⚕️ मरीज:"),
            "date": ("📅 Date:", "📅 तारीख:"),
            "meds": ("💊 Prescribed Medicines", "💊 निर्धारित दवाएं"),
            "adv": ("📝 Advice & Precautions", "📝 सलाह और सावधानियां"),
            "inv": ("🔬 Investigations", "🔬 जांचें"),
            "fup": ("📆 Follow Up", "📆 दोबारा मिलें"),
            "dx": ("📌 Diagnosis:", "📌 निदान:"),
            "sig": ("✍️ Dr. Aarogya", "✍️ डॉ. आरोग्य"),
            "footer": ("_AI-generated prescription for informational purposes. Consult a qualified doctor._",
                      "_जानकारी के लिए AI-जनित पर्चा। कृपया योग्य डॉक्टर से सलाह लें।_")
        }

        md = []
        md.append(f"### {labels['rx_title'][idx]}")
        md.append("---")
        md.append(f"**{labels['name'][idx]}**")
        md.append(f"*{labels['qual'][idx]}*")
        md.append(f"*{labels['hosp'][idx]}*")
        md.append(f"*{labels['reg'][idx]}*")
        md.append("---")
        md.append(
            f"{labels['patient'][idx]} **{self.patient_name}**  |  {labels['date'][idx]} {self.date.strftime('%d-%b-%Y %H:%M')}")
        md.append("---")

        if self.medicines:
            md.append(f"#### {labels['meds'][idx]}")
            md.append("| # | Medicine | Dosage | Timing | Duration | Note |")
            md.append("|---|----------|--------|--------|----------|------|")
            for i, med in enumerate(self.medicines, 1):
                name = med.get("name", "")
                dosage = med.get("dosage", "")
                timing = med.get("timing", med.get("timing", ""))
                duration = med.get("duration", "")
                note = med.get("note", "")
                md.append(
                    f"| {i} | {name} | {dosage} | {timing} | {duration} | {note} |")

        if self.advice:
            md.append(f"\n#### {labels['adv'][idx]}")
            for adv in self.advice:
                md.append(f"- ✅ {adv}")

        if self.investigations:
            md.append(f"\n#### {labels['inv'][idx]}")
            for inv in self.investigations:
                md.append(f"- {inv}")

        if self.follow_up:
            md.append(
                f"\n#### {labels['fup'][idx]}  \n{self.follow_up}")

        md.append("\n---")
        md.append(f"{labels['sig'][idx]}")
        md.append(f"\n{labels['footer'][idx]}")

        return "\n".join(md)
