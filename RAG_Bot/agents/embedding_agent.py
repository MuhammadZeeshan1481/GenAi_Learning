from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from constants import EMBEDDING_MODEL

class EmbeddingAgent:
    def __init__(self):
        self.embedder = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    def run(self, chunks):
        return FAISS.from_texts(chunks, self.embedder)
