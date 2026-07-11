import streamlit as st
import requests
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="AI Language Translation",
    page_icon="🌍",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #050816 0%, #0f172a 100%);
        color: white;
    }
    section[data-testid="stSidebar"] {
        background: #0b1120;
        border-right: 1px solid rgba(255,255,255,0.08);
    }
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        color: white;
        margin-bottom: 0.5rem;
        letter-spacing: -2px;
    }
    .gradient {
        background: linear-gradient(90deg,#60a5fa,#22d3ee);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #94a3b8;
        margin-bottom: 1rem;
        line-height: 1.6;
    }
    .glass {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
        padding: 2rem;
        border-radius: 24px;
        backdrop-filter: blur(14px);
        margin-bottom: 2rem;
    }
    .metric-card {
        background: rgba(255,255,255,0.05);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.08);
    }
    .result-box {
        background: rgba(15,23,42,0.8);
        border: 1px solid rgba(96,165,250,0.3);
        border-radius: 20px;
        padding: 2rem;
        font-size: 1.2rem;
        color: white;
    }
    .feature-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        padding: 0.8rem;
        border-radius: 12px;
        margin-bottom: 0.5rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

API_BASE_URL = "https://ai-language-translation-backendd.onrender.com"
#http://127.0.0.1:8000
# ---------------- SIDEBAR ---------------- #
with st.sidebar:
    st.markdown("# 🌍 AI Translation")
    st.markdown("---")
    st.markdown("## 🔐 Authentication")
    
    auth_option = st.radio("Choose Option", ["Login", "Register"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if auth_option == "Register":
        username = st.text_input("Username")
        if st.button("Register User"):
            try:
                response = requests.post(f"{API_BASE_URL}/register", 
                                      json={"username": username, "email": email, "password": password})
                st.success(response.json().get("Message", "Registered!"))
            except Exception as e:
                st.error(f"Connection failed: {e}")
    else:
        if st.button("Login"):
            try:
                response = requests.post(f"{API_BASE_URL}/login", 
                                      json={"email": email, "password": password})
                data = response.json()
                if "access_token" in data:
                    st.session_state["token"] = data["access_token"]
                    st.success("Logged in")
                    # st.rerun()
                    #success = True
                else:
                    st.error("Invalid credentials")
            except:
                st.error("Connection failed")
            # if success:
            #     st.success("Logged in")
            #     st.rerun()
    
    st.markdown("---")
    st.markdown("## 🚀 Platform Features")
    features = ["JWT Authentication", "Translation History", "PDF Export", "Rate Limiting", "Swagger Documentation", "MySQL Integration", "Global Exception Handling"]
    for f in features:
        st.markdown(f"✅ {f}")

# ---------------- HEADER ---------------- #
st.markdown(
    f"""
    <div class="glass">
        <h1 class="main-title">AI Language <span class="gradient">Translation</span></h1>
        <p class="subtitle">
            Professional multilingual translation platform built using FastAPI,
            MySQL, JWT Authentication and NLP-based translation services.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- METRICS ---------------- #
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
metrics = [("100+", "Languages"), ("JWT", "Secure Auth"), ("PDF", "Exports"), ("API", "FastAPI")]
for col, (val, label) in zip([m_col1, m_col2, m_col3, m_col4], metrics):
    col.markdown(f'<div class="metric-card"><h1>{val}</h1><p>{label}</p></div>', unsafe_allow_html=True)

# ---------------- TRANSLATION SECTION ---------------- #
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-cn",
    "Arabic": "ar",
    "Russian": "ru",
    "Portuguese": "pt",
    "Turkish": "tr",
    "Dutch": "nl",
    "Greek": "el",
    "Polish": "pl",
    "Swedish": "sv",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Urdu": "ur",
    "Punjabi": "pa",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Bengali": "bn",
    "Nepali": "ne",
    "Sinhala": "si",
    "Persian": "fa",
    "Hebrew": "he",
    "Ukrainian": "uk",
    "Romanian": "ro",
    "Hungarian": "hu",
    "Czech": "cs",
    "Danish": "da",
    "Finnish": "fi",
    "Norwegian": "no",
    "Slovak": "sk",
    "Croatian": "hr",
    "Serbian": "sr",
    "Bulgarian": "bg",
    "Malay": "ms",
    "Swahili": "sw",
    "Filipino": "tl",
    "Latin": "la",
    "Estonian": "et",
    "Lithuanian": "lt",
    "Latvian": "lv",
    "Slovenian": "sl",
    "Icelandic": "is",
    "Irish": "ga",
    "Welsh": "cy",
    "Albanian": "sq",
    "Mongolian": "mn",
    "Georgian": "ka",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Kazakh": "kk",
    "Uzbek": "uz"
} # Add more as needed

st.write("")

st.markdown("## 🌍 Translate Text")

src = st.selectbox(
    "Source",
    options=list(languages.keys()),
    index=0,
    placeholder="Search source language..."
)

tgt = st.selectbox(
    "Target",
    options=list(languages.keys()),
    index=1,
    placeholder="Search target language..."
)

text = st.text_area("Enter Text", height=150)

if st.button("Translate Now", use_container_width=True):
    if "token" not in st.session_state:
        st.error("Please login first")
    elif text.strip():
        try:
            headers = {
                "Authorization": f"Bearer {st.session_state['token']}"
            }

            resp = requests.post(
                f"{API_BASE_URL}/translate",
                headers=headers,
                json={
                    "text": text,
                    "source_lang": languages[src],
                    "target_lang": languages[tgt]
                }
            )

            res_data = resp.json()

            st.markdown(
                f'<div class="result-box">{res_data.get("translated_text", "Error in response")}</div>',
                unsafe_allow_html=True
            )

        except:
            st.error("Translation failed")

# ---------------- HISTORY SECTION (AS SEEN IN SCREENSHOT) ---------------- #
st.markdown('<div class="section-header">📜 Translation History</div>', unsafe_allow_html=True)

if st.button("Load Translation History"):
    if "token" in st.session_state:
        try:
            headers = {"Authorization": f"Bearer {st.session_state['token']}"}
            history_data = requests.get(f"{API_BASE_URL}/history", headers=headers).json()
            if history_data:
                st.dataframe(pd.DataFrame(history_data), use_container_width=True)
            else:
                st.info("No history found.")
        except:
            st.error("Failed to fetch history.")
    else:
        st.warning("Please login first.")

# ---------------- EXPORT SECTION (AS SEEN IN SCREENSHOT) ---------------- #
st.markdown('<div class="section-header">📄 Export Translation History</div>', unsafe_allow_html=True)

if "token" in st.session_state:
    try:
        headers = {"Authorization": f"Bearer {st.session_state['token']}"}
        pdf_resp = requests.get(f"{API_BASE_URL}/export-history", headers=headers)
        if pdf_resp.status_code == 200:
            st.download_button(
                label="Download PDF History",
                data=pdf_resp.content,
                file_name="translation_history.pdf",
                mime="application/pdf"
            )
    except:
        st.error("Export service unavailable.")
else:
    st.button("Download PDF History", disabled=True, help="Login to enable download")

# ---------------- FOOTER ---------------- #
st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; color:#64748b; padding:20px;">
        AI Language Translation Platform • Developed using FastAPI and Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
