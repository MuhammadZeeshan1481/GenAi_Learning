from constants import QA_MODEL
from transformers import pipeline, AutoTokenizer
from langchain_core.documents import Document
from utils.history_store import save_query_answer
from streamlit import session_state

class QAAgent:
    def __init__(self, retriever):
        self.retriever = retriever
        self.model = QA_MODEL
        self.pipe = pipeline("text2text-generation", model=self.model)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model)

    def run(self, query, filepath=None, return_sources=False):
        retriever = self.retriever.as_retriever()
        docs = retriever.invoke(query)

        # Token-safe context build
        max_input_tokens = 512
        context_parts = []
        total_tokens = 0

        for doc in docs:
            tokens = self.tokenizer.encode(doc.page_content, truncation=False)
            if total_tokens + len(tokens) > max_input_tokens:
                break
            context_parts.append(doc.page_content)
            total_tokens += len(tokens)

        context = "\n\n".join(context_parts)
        prompt = f"Answer the question based on the context.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"

        output = self.pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7)
        answer = output[0]["generated_text"].strip()

        if filepath:
            save_query_answer(filepath, query, answer)

        if return_sources:
            return answer, docs
        return answer
