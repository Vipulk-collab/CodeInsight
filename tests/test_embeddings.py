import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from shared.encoder import encode_documents
from shared.encoder import (
    encode_documents
)

texts = [

    "def login(username,password)",

    "def create_user(email,password)"
]

embeddings = encode_documents(
    texts
)

print(
    "Shape:",
    embeddings.shape
)

print(
    "First Vector Length:",
    len(embeddings[0])
)