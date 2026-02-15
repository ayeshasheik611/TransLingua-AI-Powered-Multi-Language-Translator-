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
    
    # List available models and use the first gemini model found
    try:
        models = genai.list_models()
        gemini_models = [m for m in models if 'gemini' in m.name.lower() and 'generateContent' in m.supported_generation_methods]
        if gemini_models:
            model_name = gemini_models[0].name
            return genai.GenerativeModel(model_name)
    except:
        pass
    
    # Fallback to common model names
    for model_name in ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro', 'gemini-1.0-pro']:
        try:
            return genai.GenerativeModel(model_name)
        except:
            continue
    
    st.error("❌ No compatible Gemini model found. Please check your API key.")
    st.stop()

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
col1, col2 = st.columns([1, 1])

with col1:
    source_language = st.selectbox(
        "Source Language",
        LANGUAGES,
        index=0,
        key="source"
    )

with col2:
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
    
    # Display translated text in a text area for better visibility and copying
    st.text_area(
        label="Translation",
        value=st.session_state['translated_text'],
        height=150,
        key="translation_output",
        label_visibility="collapsed"
    )
    
    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📋 Copy to Clipboard", use_container_width=True):
            st.success("✅ Select the text above and copy it (Ctrl+C or Cmd+C)")
    
    with col2:
        if st.button("🗑️ Clear", use_container_width=True):
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
