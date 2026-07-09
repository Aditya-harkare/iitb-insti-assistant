from src.vector_db import load_index
from src.config import VECTOR_DIR

from src.retriever import retrieve
from src.llm import generate_answer

index, metadata = load_index(VECTOR_DIR)


def ask(question):

    retrieved = retrieve(question, index, metadata, top_k=8)

    if len(retrieved) == 0:
        return (
            "I don't know based on the provided IIT Bombay documents.",
            []
        )

    answer = generate_answer(question, retrieved)

    return answer, retrieved