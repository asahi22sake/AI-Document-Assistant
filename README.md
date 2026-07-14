# AI Document Assistant

An AI-powered document assistant that enables users to upload documents, generate embeddings, perform semantic search, and interact with documents through a chatbot using Retrieval-Augmented Generation (RAG).

## Features

- 📄 Upload PDF documents
- ✂️ Split documents into text chunks
- 🧠 Generate embeddings
- 📦 Store embeddings using ChromaDB
- 🔍 Semantic search
- 💬 AI-powered question answering using RAG

## Tech Stack

- Python
- LangChain
- ChromaDB
- OpenAI / Gemini API
- Vector Embeddings

## Project Structure

```
AI-Document-Assistant/
│── app.py
│── chatbot.py
│── embeddings.py
│── loader.py
│── splitter.py
│── vector_store.py
│── test.py
│── requirements.txt
│── README.md
│── data/
```

## Installation

```bash
git clone https://github.com/asahi22sake/AI-Document-Assistant.git

cd AI-Document-Assistant

python -m venv venv

source venv/bin/activate      # macOS/Linux

pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Future Improvements

- Support multiple document formats
- Chat history
- Authentication
- Better UI
- Cloud deployment

## Author

**Anshul Malwal**