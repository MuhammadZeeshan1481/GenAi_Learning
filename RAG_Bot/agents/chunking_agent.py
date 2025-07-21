from langchain.text_splitter import RecursiveCharacterTextSplitter
from constants import CHUNK_SIZE, CHUNK_OVERLAP

class ChunkingAgent:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )

    def run(self, text: str):
        return self.splitter.split_text(text)
