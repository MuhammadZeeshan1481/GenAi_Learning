import fitz  
from typing import List, Tuple

class PDFLoaderAgent:
    def __init__(self):
        pass

    def run(self, file_path: str) -> Tuple[str, List[str]]:
        doc = fitz.open(file_path)
        all_text = []
        page_texts = []

        for page in doc:
            text = page.get_text()
            page_texts.append(text)
            all_text.append(f"[Page {page.number + 1}]\n{text}")

        combined_text = "\n".join(all_text)
        return combined_text, page_texts
