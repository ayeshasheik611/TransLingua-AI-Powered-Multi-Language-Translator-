import streamlit as st
import os
import google.generativeai as genai

# Try to load dotenv only if available (for local development)
try:
    from dotenv import load_dotenv
    load_dotenv('backend/.env')
except ImportError:
    pass  # dotenv not available, will use Streamlit secrets instead

# Configure page
st.set_page_config(
    page_title="TransLingua - AI Translator",
    page_icon="🌐",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stTextArea textarea {
        font-size: 16px;
    }
    h1 {
        text-align: center;
        color: #667eea;
    }
    .success-box {
        padding: 20px;
        background-color: #f0f2f6;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Gemini client
@st.cache_resource
def get_gemini_model():
    # Try to get API key from Streamlit secrets first, then from environment variable
    api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        st.error("⚠️ GEMINI_API_KEY not found. Please add it to Streamlit secrets")
        st.stop()
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('models/gemini-1.5-flash')

model = get_gemini_model()

# Translation function
def translate_text(text, source_language, target_language):
    """
    Translate text from source language to target language using Gemini AI
    """
    prompt = (
        f"Translate the following text from {source_language} to {target_language}. "
        f"Provide only the translation without any additional explanation or context.\n\n"
        f"Text: {text}"
    )
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Language options
LANGUAGES = [
    "English",
    "Spanish",
    "French",
    "German",
    "Chinese",
    "Hindi",
    "Japanese",
    "Korean",
    "Portuguese",
    "Italian",
    "Russian",
    "Arabic",
    "Dutch",
    "Turkish",
    "Polish",
    "Vietnamese",
]

# Header
st.title("🌐 TransLingua")
st.markdown("### AI-Powered Language Translator")
st.markdown("---")

# Create two columns for language selection
col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    source_language = st.selectbox(
        "Source Language",
        LANGUAGES,
        index=0,
        key="source"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄", help="Swap languages"):
        # Swap languages
        temp = st.session_state.get('source_language', source_language)
        st.session_state['source_language'] = st.session_state.get('target_language', 'French')
        st.session_state['target_language'] = temp
        st.rerun()

with col3:
    target_language = st.selectbox(
        "Target Language",
        LANGUAGES,
        index=2,
        key="target"
    )

st.markdown("---")

# Input text area
input_text = st.text_area(
    "Enter text to translate:",
    height=150,
    max_chars=5000,
    placeholder="Type or paste your text here...",
    help="Maximum 5000 characters"
)

# Character count
if input_text:
    st.caption(f"Characters: {len(input_text)}/5000")

# Translate button
if st.button("🚀 Translate", type="primary", use_container_width=True):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text to translate.")
    elif source_language == target_language:
        st.warning("⚠️ Source and target languages must be different.")
    else:
        with st.spinner("Translating..."):
            translated_text = translate_text(input_text, source_language, target_language)
            
            # Store in session state
            st.session_state['translated_text'] = translated_text
            st.session_state['last_input'] = input_text

# Display translation result
if 'translated_text' in st.session_state:
    st.markdown("---")
    st.markdown("### 📝 Translated Text")
    
    # Display in a nice box
    st.markdown(f"""
        <div class="success-box">
            <p style="font-size: 18px; line-height: 1.6; margin: 0;">
                {st.session_state['translated_text']}
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📋 Copy to Clipboard"):
            st.code(st.session_state['translated_text'], language=None)
            st.success("✅ Text ready to copy!")
    
    with col2:
        if st.button("🗑️ Clear"):
            del st.session_state['translated_text']
            if 'last_input' in st.session_state:
                del st.session_state['last_input']
            st.rerun()

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666; font-size: 12px;'>Powered by Google Gemini AI • TransLingua © 2026</p>",
    unsafe_allow_html=True
)
