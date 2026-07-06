# Dr. Aarogya - AI Medical Doctor

This project is an AI medical doctor chatbot called **Dr. Aarogya**. Key facts:

## Project Location
- Root: `C:\Users\Admin\projects\ai-doctor`
- GitHub: `https://github.com/mohitanandofficial11-eng/ai-doctor`
- Deployed: `https://ai-doctor-ikhyvks5vtva9g7scjzzkg.streamlit.app`

## Key Files
- `app.py` — Main Streamlit UI
- `core/doctor_ai.py` — AI logic (Groq Llama 3.3 70B + rule-based fallback)
- `core/knowledge_base.py` — Symptoms, medicines, doctor profile data
- `core/hinglish.py` — Hinglish language detection
- `core/prescription_gen.py` — Prescription PDF generation
- `requirements.txt` — Dependencies

## Tech Stack
- **Frontend**: Streamlit (Python)
- **AI**: Groq API (Llama 3.3 70B) via `groq` Python package
- **Hosting**: Streamlit Cloud (free tier, sleeps on inactivity)
- **Version Control**: Git + GitHub

## Status
- All code committed and pushed to GitHub main branch
- Auto-deploys to Streamlit Cloud on push
