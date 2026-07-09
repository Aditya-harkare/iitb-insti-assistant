import numpy as np

from src.embedder import model


SIMILARITY_THRESHOLD = 0.55      # Tune after testing


def retrieve(query, index, metadata, top_k=5):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    scores, indices = index.search(query_embedding, top_k)

    results = []

    for idx, score in zip(indices[0], scores[0]):

        if idx == -1:
            continue

        chunk = metadata[idx].copy()
        chunk["score"] = float(score)

        results.append(chunk)

    print("\nRetrieved Chunks:")
    for r in results:
        print(f"{r['source']} | Page {r.get('page', '-')}")
        print(r["text"][:250])
        print("-" * 60)

    return results