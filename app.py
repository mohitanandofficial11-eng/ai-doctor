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
    .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
    .main-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d6a9f 100%);
        color: white; padding: 1.5rem; border-radius: 15px;
        text-align: center; margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .main-header h1 { margin: 0; font-weight: 700; font-size: 2.2rem; letter-spacing: 0.5px; }
    .main-header p { margin: 5px 0 0; opacity: 0.9; font-size: 1rem; }
    .chat-message {
        padding: 1rem 1.2rem; border-radius: 15px; margin-bottom: 0.8rem;
        max-width: 85%; line-height: 1.6; font-size: 0.95rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.08);
    }
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white; margin-left: auto; border-bottom-right-radius: 5px;
    }
    .doctor-message {
        background: white; color: #1a1a2e; margin-right: auto;
        border-bottom-left-radius: 5px; border-left: 4px solid #2d6a9f;
    }
    .doctor-message strong { color: #1e3a5f; }
    .emergency-banner {
        background: linear-gradient(135deg, #ff4757 0%, #c0392b 100%);
        color: white; padding: 1rem; border-radius: 10px;
        text-align: center; font-weight: 600; font-size: 1.1rem;
        animation: pulse 1.5s infinite; margin: 0.5rem 0;
    }
    @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.01); } 100% { transform: scale(1); } }
    .sidebar-widget {
        background: white; border-radius: 12px; padding: 1rem;
        margin-bottom: 1rem; box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .sidebar-widget h4 { color: #1e3a5f; margin-top: 0; }
    .stTextInput>div>div>input {
        border-radius: 25px !important; border: 2px solid #e0e0e0 !important;
        padding: 12px 20px !important; font-size: 1rem !important;
    }
    .stTextInput>div>div>input:focus {
        border-color: #2d6a9f !important; box-shadow: 0 0 0 3px rgba(45,106,159,0.2) !important;
    }
    div[data-testid="stHorizontalBlock"] { gap: 1rem; }
    .stButton>button {
        border-radius: 25px; background: linear-gradient(135deg, #1e3a5f, #2d6a9f);
        color: white; font-weight: 500; border: none; padding: 8px 25px;
    }
    .tag {
        display: inline-block; background: #e8f0fe; color: #1e3a5f;
        padding: 3px 10px; border-radius: 12px; font-size: 0.8rem; margin: 2px;
    }
    @media (max-width: 768px) {
        .chat-message { max-width: 95%; }
        .main-header h1 { font-size: 1.5rem; }
    }
    .doctor-profile-widget {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d6a9f 100%);
        color: white; border-radius: 15px; padding: 1.2rem;
        margin-bottom: 1rem; box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    .doctor-profile-widget h4 {
        color: white; margin-top: 0; font-size: 1.2rem;
        border-bottom: 2px solid rgba(255,255,255,0.3);
        padding-bottom: 8px;
    }
    .doctor-profile-widget p { margin: 0.5rem 0; line-height: 1.7; }
    .doctor-profile-widget b { color: #ffd700; }
    .happy-header {
        color: #2d7d46; font-size: 1.3rem; font-weight: 700;
        padding: 5px 0; display: inline-block;
    }
    .disclaimer-footer {
        background: #fff3cd; border: 1px solid #ffc107; border-radius: 8px;
        padding: 0.8rem; text-align: center; font-size: 0.85rem; color: #856404;
        margin-top: 1.5rem;
    }
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


def new_chat():
    st.session_state.chat_counter += 1
    cid = f"chat_{st.session_state.chat_counter}"
    st.session_state.chats[cid] = {"name": f"Chat {st.session_state.chat_counter}", "messages": []}
    st.session_state.current_chat_id = cid


def switch_chat(cid):
    st.session_state.current_chat_id = cid


def sidebar_content():
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/doctor-male--v1.png", width=80)
        st.markdown("### 👨‍⚕️ Dr. Aarogya")
        st.markdown("*AI Medical Assistant*")

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
            if cid == st.session_state.current_chat_id:
                st.markdown(f"**✦ {chat['name']}**")
            else:
                if st.button(f"○ {chat['name']}", key=f"switch_{cid}", use_container_width=True):
                    switch_chat(cid)
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
              "🫁 Acidity / Gas", "😔 Depression", "🧠 Anxiety / Tension"],
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
                "Anxiety": "anxiety", "Tension": "anxiety"
            }
            selected = quick.split(" ")[-1]
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
        st.markdown("#### 🔪 Surgery Info")
        surg_name = st.text_input("Search surgery:", placeholder="e.g. Appendectomy")
        if surg_name:
            info = st.session_state.doctor.get_surgery_info(surg_name, st.session_state.lang)
            if info:
                with st.expander(f"🔪 {surg_name.title()}", expanded=True):
                    st.markdown(info)
            else:
                st.info("Surgery info not found in database")

        st.markdown("---")
        st.markdown("#### ⚠️ Disclaimer")
        st.caption(
            "Dr. Aarogya is an AI assistant for informational purposes only. "
            "Always consult a qualified doctor for medical advice. "
            "In emergencies, call 911/108 immediately."
        )


def main():
    init_session()

    st.markdown("""
    <div class="main-header">
        <h1>🏥 Dr. Aarogya — AI Medical Doctor</h1>
        <p>💬 Your 24/7 AI Health Assistant | 🇮🇳 Hinglish & English | 🔪 Surgery Knowledge</p>
    </div>
    """, unsafe_allow_html=True)

    sidebar_content()

    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown("""<span class="happy-header">💬 Chat with Dr. Aarogya</span>""", unsafe_allow_html=True)

        msgs = st.session_state.chats[st.session_state.current_chat_id]["messages"]
        chat_container = st.container()
        with chat_container:
            for chat in msgs:
                if isinstance(chat, dict):
                    if chat["role"] == "user":
                        st.markdown(f'<div class="chat-message user-message"><b>🧑 You:</b><br>{chat["message"]}</div>',
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

        if not msgs:
            st.markdown("""
            <div style="text-align:center; padding:2rem 1rem; background:white; border-radius:15px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">
                <h3 style="color:#1e3a5f; margin-bottom:10px;">👋 Welcome to Dr. Aarogya</h3>
                <p style="color:#555; margin:0;">Apna symptom batao ya koi bhi health concern likho.<br>Main English aur Hinglish dono samajhta hoon! 🙂</p>
            </div>
            """, unsafe_allow_html=True)

        user_input = st.chat_input("Type your message here...", key="chat_input")
        if user_input:
            result = st.session_state.doctor.process_message(user_input.strip())
            user_chat = {"role": "user", "message": user_input.strip()}
            msgs.append(user_chat)
            if isinstance(result, dict):
                msgs.append(result)
            else:
                msgs.append({"role": "doctor", "response": result})
            st.rerun()

    with col2:
        lang = st.session_state.lang
        prof = DOCTOR_PROFILE
        st.markdown(f"""
        <div class="doctor-profile-widget">
            <h4>👨‍⚕️ {prof['name']}</h4>
            <p><b>🎓 {"Qualification" if lang == 'en' else 'योग्यता'}:</b><br>
            {prof['qualifications'][lang]}</p>
            <p><b>💼 {"Experience" if lang == 'en' else 'अनुभव'}:</b><br>
            {prof['experience'][lang]}</p>
            <p><b>🏥</b> {prof['hospital'][lang]}<br>
            <b>📋 Reg:</b> DEL-MC-2010-04256</p>
            <p>🌐 <b>{"Languages" if lang == 'en' else 'भाषाएं'}:</b> English, Hindi, Hinglish</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 🎯 Specialties")
        tags_html = '<div style="line-height:2.2;">'
        items = [("🫀","Cardiology"),("🫁","Pulmonology"),("🧠","Neurology"),("🦴","Orthopedics"),("🩺","General"),("👁️","Eye"),("👂","ENT"),("🩸","Skin"),("🧬","Surgery")]
        for emoji, name in items:
            tags_html += f'<span class="tag">{emoji} {name}</span> '
        tags_html += '</div>'
        st.markdown(tags_html, unsafe_allow_html=True)

        st.markdown("#### 🔪 Surgery Knowledge")
        cols = st.columns(2)
        surgeris = ["Appendectomy","Cholecystectomy","Hernia Repair","CABG (Bypass)","Knee Replacement","Cataract Surgery","Spinal Fusion","Lap. Surgery"]
        for i, s in enumerate(surgeris):
            cols[i % 2].markdown(f"🔪 {s}")



    st.markdown("""
    <div class="disclaimer-footer">
        ⚠️ <b>DISCLAIMER:</b> Dr. Aarogya is an AI assistant for educational purposes only.
        Not a substitute for professional medical advice. Always consult a qualified doctor.
        In case of emergency, call 911 / 108 immediately.
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
