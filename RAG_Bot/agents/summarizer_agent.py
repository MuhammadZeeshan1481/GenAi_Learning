from transformers import pipeline

class SummarizerAgent:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def run(self, text: str) -> str:
        # Return early for short input
        if len(text.strip().split()) < 50:
            return "Input too short to summarize meaningfully."

        max_chunk_chars = 1000  # character-based chunking for simplicity
        summaries = []

        for i in range(0, len(text), max_chunk_chars):
            chunk = text[i:i + max_chunk_chars]

            # Auto-adjust max_length for short chunks
            chunk_length = len(chunk.strip().split())
            max_len = min(150, chunk_length + 20)
            min_len = max(20, int(max_len / 3))

            try:
                summary = self.summarizer(
                    chunk,
                    max_length=max_len,
                    min_length=min_len,
                    do_sample=False
                )[0]["summary_text"]
                summaries.append(summary)
            except Exception as e:
                summaries.append(f"[Error summarizing chunk: {str(e)}]")

        return "\n\n".join(summaries)
