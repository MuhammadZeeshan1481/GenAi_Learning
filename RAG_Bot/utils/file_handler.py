import os

BASE_PDF_DIR = "data/pdfs"
BASE_INDEX_DIR = "data/faiss_indexes"

def get_pdf_path(filename: str) -> str:
    return os.path.join(BASE_PDF_DIR, filename)

def ensure_dirs():
    os.makedirs(BASE_PDF_DIR, exist_ok=True)
    os.makedirs(BASE_INDEX_DIR, exist_ok=True)
