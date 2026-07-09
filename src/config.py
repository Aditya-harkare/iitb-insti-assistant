from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "raw"

VECTOR_DIR = BASE_DIR / "vector_store"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")