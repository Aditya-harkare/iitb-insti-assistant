from src.config import DATA_DIR, VECTOR_DIR
from src.ingest import load_documents
from src.chunker import chunk_documents
from src.embedder import embed_texts
from src.vector_db import create_faiss_index, save_index


documents = load_documents(DATA_DIR)

chunks = chunk_documents(documents)

texts = [c["text"] for c in chunks]

embeddings = embed_texts(texts)

index = create_faiss_index(embeddings)

save_index(index, chunks, VECTOR_DIR)

print(f"{len(chunks)} chunks indexed successfully.")