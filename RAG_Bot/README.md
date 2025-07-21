# Multi-Agent PDF RAG Bot

A multi-agent RAG (Retrieval-Augmented Generation) bot built with Streamlit, designed to process PDF documents and perform intelligent tasks such as answering questions, summarizing, and translating content.

##  Key Features

- **PDF Upload & Processing:** Extracts and indexes text using vector embeddings.
- **RAG Pipeline:** Utilizes vector similarity to retrieve relevant chunks and provide context-aware responses.
- **Multi-Agent Capabilities:**
  - **Answer Agent**
  - **Summarizer Agent**
  - **Translator Agent**
- **Language Support:** Supports multilingual translation (configurable target language).
- **Chunk Source Display:** Toggle to show/hide the source chunks of the response.

##  Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Embedding:** HuggingFace Transformers
- **Vector DB:** FAISS
- **LLM:** Open-source models (e.g., `facebook/bart-large-cnn`, `distilbart`, etc.)

##  How It Works

1. User uploads a PDF file.
2. Text is chunked and embedded into vectors.
3. User can ask questions, request summaries, or translations.
4. System routes the query through appropriate agents.
5. Responses are displayed along with source references (if enabled).

##  Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/multi-agent-rag-bot.git
cd multi-agent-rag-bot

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run demo_app.py
