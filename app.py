import streamlit as st
import sys
import os
import base64
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core.doctor_ai import MedicalDoctorAI
from core.knowledge_base import MEDICINES_DB, SURGERY_INFO, SPECIALTIES, DOCTOR_PROFILE


st.set_page_config(
    page_title="Dr. Aarogya - AI Medical Doctor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# PWA icons - use custom icon.png if exists, else fallback to SVG
ICON_PATH = os.path.join(os.path.dirname(__file__), "icon.png")
if os.path.exists(ICON_PATH):
    with open(ICON_PATH, "rb") as f:
        PWA_ICON_B64 = base64.b64encode(f.read()).decode()
    PWA_ICON_TYPE = "image/png"
else:
    PWA_ICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
<defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" style="stop-color:#1e3a5f"/><stop offset="100%" style="stop-color:#2d6a9f"/>
</linearGradient></defs>
<rect width="512" height="512" rx="100" fill="url(#g)"/>
<text x="256" y="310" text-anchor="middle" font-size="280" fill="white">🏥</text>
</svg>"""
    PWA_ICON_B64 = base64.b64encode(PWA_ICON_SVG.encode()).decode()
    PWA_ICON_TYPE = "image/svg+xml"
MANIFEST = {
    "name": "Dr. Aarogya - AI Medical Doctor",
    "short_name": "Dr. Aarogya",
    "start_url": ".",
    "display": "standalone",
    "background_color": "#1e3a5f",
    "theme_color": "#1e3a5f",
    "icons": [{"src": f"data:{PWA_ICON_TYPE};base64,{PWA_ICON_B64}", "sizes": "512x512", "type": PWA_ICON_TYPE}]
}
MANIFEST_B64 = base64.b64encode(json.dumps(MANIFEST).encode()).decode()

st.markdown(
    '<link rel="manifest" href="data:application/json;base64,' + MANIFEST_B64 + '">'
    + '<link rel="icon" href="data:' + PWA_ICON_TYPE + ';base64,' + PWA_ICON_B64 + '">'
    + '<link rel="apple-touch-icon" href="data:' + PWA_ICON_TYPE + ';base64,' + PWA_ICON_B64 + '">'
    + '<meta name="apple-mobile-web-app-capable" content="yes">'
    + '<meta name="apple-mobile-web-app-title" content="Dr. Aarogya">'
    + '<meta name="theme-color" content="#1e3a5f">',
    unsafe_allow_html=True
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background: #ffffff; }
    .main-header {
        padding: 0.6rem 1rem; text-align: center; margin-bottom: 0.5rem;
        border-bottom: 1px solid #e5e5e5;
    }
    .main-header h1 { margin: 0; font-weight: 600; font-size: 1.3rem; color: #1e3a5f; }
    .main-header p { display: none; }
    .chat-message {
        padding: 0.8rem 1rem; margin-bottom: 0.5rem;
        max-width: 90%; line-height: 1.6; font-size: 0.95rem;
    }
    .user-message {
        background: #f0f0f0; color: #1a1a1a; margin-left: auto;
        border-radius: 16px 16px 4px 16px;
    }
    .doctor-message {
        color: #1a1a1a; margin-right: auto;
        border-radius: 16px 16px 16px 4px;
    }
    .doctor-message strong { color: #1e3a5f; }
    .emergency-banner {
        background: #fee; color: #c00; padding: 0.8rem; border-radius: 10px;
        text-align: center; font-weight: 600; font-size: 1rem; margin: 0.5rem 0;
        border: 1px solid #fcc;
    }
    .stTextInput>div>div>input {
        border-radius: 25px !important; border: 1px solid #ddd !important;
        padding: 10px 16px !important; font-size: 0.95rem !important;
    }
    .stTextInput>div>div>input:focus {
        border-color: #1e3a5f !important; box-shadow: none !important;
    }
    div[data-testid="stHorizontalBlock"] { gap: 0.5rem; }
    .stButton>button {
        border-radius: 8px; background: #1e3a5f; color: white;
        font-weight: 500; border: none; padding: 6px 16px; font-size: 0.85rem;
    }
    .disclaimer-footer {
        display: none;
    }
    section[data-testid="stSidebar"] { min-width: 240px !important; }
    .stChatFloatingInputContainer { bottom: 0 !important; padding: 0.3rem !important; background: white !important; border-top: 1px solid #eee !important; }
    .stChatInputContainer { border-radius: 20px !important; border: 1px solid #ddd !important; }
    #plus-btn-wrap button {
        min-width: 28px !important; width: 28px !important; height: 28px !important;
        padding: 0 !important; font-size: 14px !important; border-radius: 50% !important;
        background: #1e3a5f !important; color: white !important; border: none !important;
        line-height: 1 !important; display: flex !important; align-items: center !important;
        justify-content: center !important; margin-bottom: 2px !important;
        box-shadow: none !important;
    }
    .attach-chip {
        display: inline-flex; align-items: center; gap: 4px;
        background: #e8f0fe; border-radius: 12px; padding: 3px 12px;
        font-size: 0.8rem; color: #1e3a5f; margin: 2px;
    }
    .attach-chip .remove {
        cursor: pointer; opacity: 0.6; margin-left: 4px;
    }
    .attach-chip .remove:hover { opacity: 1; }
</style>
""", unsafe_allow_html=True)


def init_session():
    if "doctor" not in st.session_state:
        st.session_state.doctor = MedicalDoctorAI()
    if "chats" not in st.session_state:
        st.session_state.chats = {"chat_1": {"name": "Chat 1", "messages": []}}
    if "current_chat_id" not in st.session_state:
        st.session_state.current_chat_id = "chat_1"
    if "chat_counter" not in st.session_state:
        st.session_state.chat_counter = 1
    if "user_name" not in st.session_state:
        st.session_state.user_name = ""
    if "lang" not in st.session_state:
        st.session_state.lang = "en"
    if "patient_registered" not in st.session_state:
        st.session_state.patient_registered = False
    if "show_attach" not in st.session_state:
        st.session_state.show_attach = False
    if "attachments" not in st.session_state:
        st.session_state.attachments = []


def new_chat():
    st.session_state.chat_counter += 1
    cid = f"chat_{st.session_state.chat_counter}"
    st.session_state.chats[cid] = {"name": f"Chat {st.session_state.chat_counter}", "messages": []}
    st.session_state.current_chat_id = cid
    st.session_state.patient_registered = False
    st.session_state.doctor = MedicalDoctorAI()


def switch_chat(cid):
    st.session_state.current_chat_id = cid


def sidebar_content():
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/doctor-male--v1.png", width=80)
        st.markdown("### 👨‍⚕️ Dr. Aarogya")
        st.markdown("*AI Medical Assistant*")

        # Patient info if registered
        p = st.session_state.doctor.patient_info
        if p.get("name"):
            st.markdown("---")
            info_html = f"<div style='background:#e8f4f8; border-radius:10px; padding:0.6rem; margin:0.3rem 0; font-size:0.9rem;'>"
            info_html += f"🧑 <b>{p.get('name', '')}</b>"
            if p.get("age"):
                info_html += f" | 🎂 {p['age']}"
            if p.get("weight"):
                info_html += f" | ⚖️ {p['weight']}"
            info_html += "</div>"
            st.markdown(info_html, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### 💬 Chats")
        col_new, col_cur = st.columns([3, 1])
        with col_new:
            if st.button("➕ New Chat", use_container_width=True):
                new_chat()
                st.rerun()
        with col_cur:
            if st.button("🔄", use_container_width=True, help="Refresh"):
                st.rerun()
        for cid, chat in st.session_state.chats.items():
            c1, c2 = st.columns([4, 1])
            with c1:
                if cid == st.session_state.current_chat_id:
                    st.button(f"● {chat['name']}", key=f"active_{cid}", use_container_width=True, disabled=True)
                else:
                    if st.button(f"○ {chat['name']}", key=f"switch_{cid}", use_container_width=True):
                        switch_chat(cid)
                        st.rerun()
            with c2:
                if st.button("🗑️", key=f"del_{cid}", help="Delete chat"):
                    if len(st.session_state.chats) > 1:
                        del st.session_state.chats[cid]
                        if st.session_state.current_chat_id == cid:
                            st.session_state.current_chat_id = list(st.session_state.chats.keys())[0]
                        st.rerun()
        st.markdown("---")

        st.markdown("#### 🌐 Language / भाषा")
        lang = st.selectbox(
            "Choose language",
            options=["English", "हिंदी / Hinglish"],
            index=0 if st.session_state.lang == "en" else 1,
            key="lang_selector"
        )
        st.session_state.lang = "hi" if "हिंदी" in lang else "en"

        st.markdown("---")
        st.markdown("#### 🏥 Quick Consult")
        quick = st.selectbox(
            "Select a symptom",
             ["", "🤒 Fever / Bukhar", "🤧 Cough & Cold", "💆 Headache",
              "🫃 Stomach Pain / Pet Dard", "🦴 Back Pain", "💓 Chest Pain",
              "🩸 Skin Rash", "🪨 Kidney Stone", "🫀 High BP", "🍬 Diabetes",
              "🫁 Acidity / Gas", "😔 Depression", "🧠 Anxiety / Tension",
              "🫄 UTI / Urine Infection", "🦵 Joint Pain / Jod Dard",
              "👁️ Eye Infection", "👂 Ear Infection", "💩 Constipation / Kabj",
              "😴 Insomnia / Neend", "⚡ Fatigue / Thakaan", "🩸 Period Pain",
              "🤢 Nausea / Vomiting", "🤧 Allergies"],
            key="quick_select"
        )
        if quick and st.button("Consult Now →", use_container_width=True):
            symptom_map = {
                "Fever": "fever", "Bukhar": "fever", "Cough": "cough_cold",
                "Cold": "cough_cold", "Headache": "headache",
                "Stomach": "acidity", "Pet Dard": "acidity",
                "Back Pain": "back_pain", "Chest Pain": "chest_pain",
                "Skin Rash": "skin_rash", "Kidney Stone": "kidney_stone",
                "High BP": "high_bp", "Diabetes": "diabetes",
                "Acidity": "acidity", "Gas": "acidity",
                "Depression": "depression",
                "Anxiety": "anxiety", "Tension": "anxiety",
                "UTI": "uti", "Urine": "uti", "Joint": "joint_pain",
                "Jod": "joint_pain", "Eye": "eye_infection",
                "Ear": "ear_infection", "Constipation": "constipation",
                "Kabj": "constipation", "Insomnia": "insomnia",
                "Fatigue": "fatigue", "Thakaan": "fatigue",
                "Period": "menstrual_cramps", "Pain": "menstrual_cramps",
                "Nausea": "nausea_vomiting", "Vomiting": "nausea_vomiting",
                "Allerg": "allergy",
            }
            for k, v in symptom_map.items():
                if k.lower() in quick.lower():
                    sym_id = v
                    break
            else:
                sym_id = "fever"
            result = st.session_state.doctor.process_message(
                f"I have {sym_id.replace('_', ' ')}")
            st.session_state.chats[st.session_state.current_chat_id]["messages"].append(result)
            st.rerun()

        st.markdown("---")
        st.markdown("#### 💊 Medicine Info")
        med_name = st.text_input("Search medicine:", placeholder="e.g. Paracetamol")
        if med_name:
            info = st.session_state.doctor.get_medicine_info(med_name, st.session_state.lang)
            if info:
                with st.expander(f"💊 {med_name.title()}", expanded=True):
                    st.markdown(info)
            else:
                st.info("Medicine not found in database")

        st.markdown("---")
        st.markdown("#### 🏥 Surgery Info")
        surg_name = st.text_input("Search surgery:", placeholder="e.g. Appendectomy")
        if surg_name:
            info = st.session_state.doctor.get_surgery_info(surg_name, st.session_state.lang)
            if info:
                with st.expander(f"🏥 {surg_name.title()}", expanded=True):
                    st.markdown(info)
            else:
                st.info("Surgery info not found in database")

        st.markdown("---")
        st.markdown("#### ⚠️ Disclaimer")
        st.caption(
            "AI assistant for info only. Consult a qualified doctor. "
            "🚨 Emergency: **911** (USA) | **108** (India)"
        )


def main():
    init_session()

    st.markdown("""
    <div class="main-header">
        <h1>🏥 Dr. Aarogya</h1>
    </div>
    """, unsafe_allow_html=True)

    sidebar_content()

    col1 = st.container()

    with col1:
        msgs = st.session_state.chats[st.session_state.current_chat_id]["messages"]

        # First visit: doctor asks for name automatically
        if not msgs:
            dr = st.session_state.doctor
            if dr.stage == "ask_name":
                greeting = dr._ask_name(st.session_state.lang)
                msgs.append({"role": "doctor", "response": greeting})
                st.rerun()
        chat_container = st.container()
        with chat_container:
            for chat in msgs:
                if isinstance(chat, dict):
                    if chat["role"] == "user":
                        msg_html = chat["message"]
                        if "files" in chat and chat["files"]:
                            ficons = " ".join(f'<span class="attach-chip">📎 {f}</span>' for f in chat["files"])
                            msg_html = f'{msg_html}<br><div style="margin-top:4px">{ficons}</div>'
                        st.markdown(f'<div class="chat-message user-message"><b>🧑 You:</b><br>{msg_html}</div>',
                                    unsafe_allow_html=True)
                    else:
                        content = chat.get("response", "")
                        if chat.get("emergency"):
                            st.markdown(f'<div class="emergency-banner">{content}</div>',
                                       unsafe_allow_html=True)
                        else:
                            st.markdown(f'<div class="chat-message doctor-message">👨‍⚕️ <b>Dr. Aarogya</b><br>{content}</div>',
                                       unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Show attached files as chips
        if st.session_state.attachments:
            chips = '<div style="display:flex; gap:6px; flex-wrap:wrap; padding:4px 0;">'
            for f in st.session_state.attachments:
                icon = "🖼️" if f.type and f.type.startswith("image") else "📄" if f.type == "application/pdf" else "🎬"
                chips += f'<span class="attach-chip">{icon} {f.name}</span>'
            chips += "</div>"
            st.markdown(chips, unsafe_allow_html=True)

        # Small + button left side
        st.markdown('<div id="plus-btn-wrap">', unsafe_allow_html=True)
        if st.button("➕", key="plus_btn", help="Attach files"):
            st.session_state.show_attach = not st.session_state.get("show_attach", False)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        if st.session_state.get("show_attach", False):
            uploaded = st.file_uploader(
                "Attach",
                type=["png", "jpg", "jpeg", "gif", "bmp", "svg", "pdf", "mp4", "avi", "mov", "mkv", "webm"],
                accept_multiple_files=True,
                key="file_upload",
                label_visibility="collapsed"
            )
            if uploaded:
                st.session_state.attachments = list(uploaded)
                st.session_state.show_attach = False
                st.rerun()

        user_input = st.chat_input("Type your message here...", key="chat_input")

        if user_input:
            msg = user_input.strip()
            files = st.session_state.get("attachments", [])
            if files:
                file_data = []
                for f in files:
                    f.seek(0); fbytes = f.read()
                    file_data.append({"name": f.name, "type": f.type, "bytes": fbytes})
                result = st.session_state.doctor.process_message_with_attachment(msg, file_data)
            else:
                result = st.session_state.doctor.process_message(msg)
            user_chat = {"role": "user", "message": msg, "files": [f.name for f in files] if files else []}
            msgs.append(user_chat)
            if isinstance(result, dict):
                msgs.append(result)
            else:
                msgs.append({"role": "doctor", "response": result})
            st.session_state.attachments = []
            st.rerun()

        # Specialist referral button (shows when symptoms are known)
        if msgs and st.session_state.doctor.reported_symptoms:
            col_a, col_b = st.columns([1, 3])
            with col_a:
                if st.button("👨‍⚕️ Suggest Specialist", use_container_width=True):
                    ref = st.session_state.doctor.get_specialist_referral(st.session_state.lang)
                    msgs.append({"role": "doctor", "response": ref})
                    st.rerun()

        # Prescription buttons (only after doctor has advised/given prescription)
        if msgs and st.session_state.doctor.stage == "advised":
            pdf = st.session_state.doctor.generate_prescription_pdf(st.session_state.lang)
            if pdf:
                st.download_button("📄 Download Prescription PDF", data=pdf, file_name="prescription.pdf", mime="application/pdf", use_container_width=True)



    st.markdown("""
    <div class="disclaimer-footer">
        ⚠️ <b>DISCLAIMER:</b> Dr. Aarogya is an AI assistant for informational purposes only.
        Not a substitute for professional medical advice. Always consult a qualified doctor.
        🚨 Emergency: <b>911</b> (USA) | <b>108</b> (India)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <script>
    document.addEventListener('keydown', function(e){
        if (e.key === 'Enter') {
            var el = document.activeElement;
            if (el && (el.tagName === 'TEXTAREA' || el.tagName === 'INPUT') && !e.shiftKey) {
                setTimeout(function(){ el.blur(); }, 50);
            }
        }
    });
    function scrollToInput() {
        var el = document.querySelector('[data-testid="stChatInput"]');
        if (el) setTimeout(function(){ el.scrollIntoView({ behavior: 'smooth', block: 'center' }); }, 400);
    }
    var observer = new MutationObserver(scrollToInput);
    var main = document.querySelector('.main');
    if (main) observer.observe(main, { childList: true, subtree: true });
    </script>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
