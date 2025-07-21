import streamlit as st
import os
from utils.file_handler import BASE_PDF_DIR

def render_uploader():
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_file:
        os.makedirs(BASE_PDF_DIR, exist_ok=True)
        file_path = os.path.join(BASE_PDF_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success(f"{uploaded_file.name} uploaded successfully.")
        return file_path
    return None
