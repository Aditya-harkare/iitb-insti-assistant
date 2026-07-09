# 🎓 IITB Insti-Assist

A Retrieval-Augmented Generation (RAG) based academic assistant for IIT Bombay that answers student queries using official institute documents. The system retrieves relevant information from a vector database built over academic PDFs and generates grounded responses using Gemini 2.5 Flash.

---

## Features

- 📄 Parses and indexes multiple IIT Bombay academic PDF documents
- ✂️ Chunks documents using Recursive Character Text Splitting
- 🧠 Generates semantic embeddings using Sentence Transformers
- ⚡ Stores and retrieves embeddings using FAISS
- 🤖 Uses Gemini 2.5 Flash to generate context-grounded answers
- 📚 Displays supporting document names and page numbers for transparency
- 🌐 Interactive Streamlit-based user interface

---

## Project Architecture

```
                    IIT Bombay PDF Documents
                               │
                               ▼
                     PDF Text Extraction
                               │
                               ▼
                        Text Chunking
                               │
                               ▼
                  Sentence Transformer Embeddings
                               │
                               ▼
                      FAISS Vector Database
                               │
                  User Question Embedding
                               │
                               ▼
                  Semantic Similarity Search
                               │
                               ▼
                  Retrieved Context Chunks
                               │
                               ▼
                     Gemini 2.5 Flash LLM
                               │
                               ▼
                     Grounded Final Answer
```

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| LLM | Gemini 2.5 Flash |
| Embedding Model | sentence-transformers (all-MiniLM-L6-v2) |
| Vector Database | FAISS |
| PDF Parsing | pdfplumber |
| Chunking | LangChain RecursiveCharacterTextSplitter |
| Language | Python |

---

## Project Structure

```text
iitb-insti-assistant/
│
├── app.py
├── build_index.py
├── requirements.txt
├── .env
│
├── data/
│   └── raw/
│       ├── *.pdf
│
├── vector_store/
│
└── src/
    ├── config.py
    ├── ingest.py
    ├── chunker.py
    ├── embedder.py
    ├── vector_db.py
    ├── retriever.py
    ├── llm.py
    └── rag_pipeline.py
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/iitb-insti-assistant.git
cd iitb-insti-assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Build the Vector Database

```bash
python build_index.py
```

This extracts text from the PDF documents, creates semantic chunks, generates embeddings, and stores them in a FAISS vector database.

---

## Run the Application

```bash
streamlit run app.py
```

The application will be available at

```
http://localhost:8501
```

---

## Example Queries

- When does the Autumn Semester begin?
- What is the penalty for using a mobile phone during examinations?
- Explain the President of India Medal.
- What is the eligibility criteria for Institute Silver Medal?
- What are the rules regarding academic malpractices?

---

## How It Works

1. Official IIT Bombay PDF documents are parsed.
2. Documents are split into overlapping text chunks.
3. Each chunk is converted into a semantic embedding.
4. Embeddings are indexed using FAISS.
5. A user's query is embedded into the same vector space.
6. Relevant chunks are retrieved using similarity search.
7. Retrieved context is provided to Gemini 2.5 Flash.
8. The assistant generates a grounded answer along with the supporting document sources.

---

## Future Improvements

- Cross-Encoder based reranking
- Hybrid keyword + semantic retrieval
- OCR support for scanned PDFs
- Chat history and conversational memory
- Multi-modal document support
- Evaluation metrics for retrieval quality

---

## License

This project was developed for educational purposes.