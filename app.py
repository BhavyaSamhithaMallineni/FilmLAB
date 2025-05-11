import streamlit as st
import base64
from format_checker import run_format_checker

# Custom CSS for mustard yellow and teal blue
custom_css = '''
<style>
    body {
        background-color: #fffaf0;
    }
    .stApp {
        background-color: #fdf6e3;
    }
    .main {
        background-color: #fdf6e3;
        color: #004d4d;
    }
    h1, h2, h3 {
        color: #004d4d;
    }
    .st-bw, .st-cq, .st-co {
        background-color: #f4d35e !important;
        color: #004d4d !important;
        border-radius: 5px;
    }
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #004d4d !important;
    }
    .stButton>button {
        background-color: #00a896 !important;
        color: white !important;
        border-radius: 5px;
    }
    .stFileUploader label {
        color: #004d4d;
        font-weight: bold;
    }
</style>
'''

st.set_page_config(page_title="ScriptWhisper", layout="wide")
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🎬 ScriptWhisper")
page = st.sidebar.radio("Navigate", ["Upload Script", "Format Checker", "Emotion Analyzer", "Story Structure", "Dialogue Helper"])

st.title("🎥 ScriptWhisper: AI-Powered Screenplay Assistant")

# Upload Page
if page == "Upload Script":
    st.header("Upload Your Screenplay")
    uploaded_file = st.file_uploader("Choose a .txt or .pdf file", type=["txt", "pdf"])
    if uploaded_file:
        file_content = uploaded_file.read()
        if uploaded_file.name.endswith(".pdf"):
            import fitz  # PyMuPDF
            doc = fitz.open(stream=file_content, filetype="pdf")
            text = "\n".join(page.get_text() for page in doc)
        else:
            text = file_content.decode("utf-8")
        
        st.session_state["script_text"] = text
        st.success("Script loaded successfully!")
        st.text_area("Screenplay Preview", text, height=400)

# Format Checker
elif page == "Format Checker":
    st.header("📐 Format Checker")
    if "script_text" not in st.session_state:
        st.warning("Please upload a script first.")
    else:
        st.subheader("Running Format Checker...")
        lines = st.session_state["script_text"].split("\n")
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        issues = run_format_checker(cleaned_lines)
        if issues:
            for lineno, msg in issues:
                st.warning(f"Line {lineno}: {msg}")
        else:
            st.success("No formatting issues found! ✅")

# Placeholder Pages
elif page == "Emotion Analyzer":
    st.header("💔 Emotion Analyzer")
    st.info("This feature will plot emotional highs and lows across the screenplay.")

elif page == "Story Structure":
    st.header("🧱 Story Structure Validator")
    st.info("This feature will identify act structure and major plot points.")

elif page == "Dialogue Helper":
    st.header("🗣️ Dialogue Enhancer")
    st.info("This feature will analyze and suggest improvements for dialogue.")