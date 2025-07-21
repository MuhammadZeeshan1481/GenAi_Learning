import streamlit as st

def render_sidebar():
    st.sidebar.title("RAG Bot Settings")
    st.sidebar.markdown("Select your interaction preferences.")

    mode = st.sidebar.radio(
        "Response Mode",
        ["Answer", "Summarize", "Translate", "Summarize → Translate → Answer"],
        index=0
    )

    target_lang = None
    if "Translate" in mode:
        target_lang = st.sidebar.selectbox("Target Language", ["fr", "es", "de", "ur", "zh", "ar", "hi"])

    show_sources = st.sidebar.checkbox("Show Source Chunks", value=True)

    return mode, target_lang, show_sources
