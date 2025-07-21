from agents.pdf_loader_agent import PDFLoaderAgent
from agents.chunking_agent import ChunkingAgent
from agents.embedding_agent import EmbeddingAgent
from agents.qa_agent import QAAgent

from utils.config_loader import load_env
from utils.logger import log_info
from utils.file_handler import get_pdf_path

def main():
    load_env()
    raw_text, _ = PDFLoaderAgent().run(get_pdf_path("sample.pdf"))
    chunks = ChunkingAgent().run(raw_text)
    vector_db = EmbeddingAgent().run(chunks)
    qa_agent = QAAgent(vector_db)

    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() in ['exit', 'quit']:
            print("Exiting RAG Bot.")
            break
        print("\nAnswer:", qa_agent.run(query))

if __name__ == "__main__":
    main()
