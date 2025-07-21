import streamlit as st

def render_query_box():
    st.markdown("### Ask a Question")
    return st.text_input("Enter your query:")
