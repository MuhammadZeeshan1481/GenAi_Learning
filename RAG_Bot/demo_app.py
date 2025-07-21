import streamlit as st
from agents.pdf_loader_agent import PDFLoaderAgent
from agents.chunking_agent import ChunkingAgent
from agents.embedding_agent import EmbeddingAgent
from agents.qa_agent import QAAgent
from agents.summarizer_agent import SummarizerAgent
from agents.translator_agent import TranslatorAgent

from components.sidebar import render_sidebar
from components.uploader import render_uploader
from components.query_box import render_query_box
from utils.config_loader import load_env
from utils.logger import log_info

def main():
    st.set_page_config(page_title="Multi-Agent PDF RAG Bot", layout="wide")
    st.title("Multi-Agent PDF RAG Bot")

    load_env()
    mode, target_lang, show_sources = render_sidebar()
    file_path = render_uploader()

    if file_path:
        st.session_state.uploaded_file_path = file_path

        if "vector_db" not in st.session_state:
            with st.spinner("Processing PDF..."):
                raw_text, file_hash = PDFLoaderAgent().run(file_path)
                chunks = ChunkingAgent().run(raw_text)
                vector_db = EmbeddingAgent().run(chunks)

                st.session_state.vector_db = vector_db
                st.session_state.raw_text = raw_text
                st.session_state.file_hash = file_hash
                log_info("PDF processed and vector index ready.")

        query = render_query_box()
        if query:
            st.markdown("#### Response:")

            def stream_output(output):
                if hasattr(output, "__iter__") and not isinstance(output, str):
                    for part in output:
                        st.write(part)
                else:
                    st.write(output)

            if mode == "Answer":
                result = QAAgent(st.session_state.vector_db).run(
                    query,
                    filepath=st.session_state.uploaded_file_path,
                    return_sources=False
                )
                stream_output(result)

            elif mode == "Summarize":
                summary = SummarizerAgent().run(st.session_state.raw_text)
                st.write(summary)

            elif mode == "Translate":
                result = QAAgent(st.session_state.vector_db).run(query, return_sources=False)
                text = "".join(result) if isinstance(result, list) else result
                translation = TranslatorAgent(target_lang).run(text)
                st.write(translation)

            elif mode == "Summarize → Translate → Answer":
                summary = SummarizerAgent().run(st.session_state.raw_text)
                st.write("**Summary:**")
                st.write(summary)
                translation = TranslatorAgent(target_lang).run(summary)
                st.write("**Translation:**")
                st.write(translation)
                result = QAAgent(st.session_state.vector_db).run(
                    query,
                    filepath=st.session_state.uploaded_file_path
                )
                stream_output(result)

            if show_sources and mode.startswith("Answer"):
                _, sources = QAAgent(st.session_state.vector_db).run(query, return_sources=True)
                st.markdown("#### Sources:")
                for i, src in enumerate(sources, 1):
                    st.info(f"**Source {i}:** {src.page_content}")

if __name__ == "__main__":
    main()
