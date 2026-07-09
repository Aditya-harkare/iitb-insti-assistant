import faiss
import pickle
import numpy as np
from pathlib import Path


def create_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index


def save_index(index, metadata, save_dir):

    Path(save_dir).mkdir(exist_ok=True)

    faiss.write_index(index, str(Path(save_dir) / "faiss.index"))

    with open(Path(save_dir) / "metadata.pkl", "wb") as f:
        pickle.dump(metadata, f)


def load_index(save_dir):

    index = faiss.read_index(str(Path(save_dir) / "faiss.index"))

    with open(Path(save_dir) / "metadata.pkl", "rb") as f:
        metadata = pickle.load(f)

    return index, metadata