import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from ingestion.github_loader import (
    get_python_files
)

from parser.ast_parser import (
    parse_python_file
)

from chunking.chunk_builder import (
    create_chunks_from_nodes
)

from shared.encoder import (
    encode_documents
)

from storage.chroma_store import (
    get_collection,
    upsert_chunks
)

repo_path = "data/repos/requests"

all_chunks = []

files = get_python_files(
    repo_path
)

for file in files:

    nodes = parse_python_file(
        str(file)
    )

    chunks = create_chunks_from_nodes(
        nodes,
        str(file),
        repo_path
    )

    all_chunks.extend(
        chunks
    )

texts = [
    chunk["code_text"]
    for chunk in all_chunks
]

embeddings = encode_documents(
    texts
)

collection = get_collection(
    "requests"
)

upsert_chunks(
    collection,
    all_chunks,
    embeddings
)

print(
    "Stored:",
    len(all_chunks)
)