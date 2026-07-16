import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from storage.chroma_store import (
    get_collection
)

collection = get_collection(
    "requests"
)

print(collection.name)
def upsert_chunks(
    collection,
    chunks,
    embeddings
):

    ids = []

    documents = []

    metadatas = []

    for chunk in chunks:

        ids.append(
            chunk["id"]
        )

        documents.append(
            chunk["code_text"]
        )

        metadatas.append(
            {
                "file_path":
                chunk["file_path"],

                "function_name":
                chunk["function_name"],

                "start_line":
                chunk["start_line"],

                "end_line":
                chunk["end_line"]
            }
        )

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )