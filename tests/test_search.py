import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from shared.encoder import (
    encode_query
)

from storage.chroma_store import (
    get_collection,
    search_chunks
)

query = (
    "function that sends HTTP requests"
)

query_embedding = (
    encode_query(query)
)

collection = (
    get_collection("requests")
)

results = search_chunks(
    collection,
    query_embedding,
    top_k=3
)

for i in range(
    len(results["documents"][0])
):

    print(
        "\n===================="
    )

    print(
        "Function:",
        results["metadatas"][0][i][
            "function_name"
        ]
    )

    print(
        "File:",
        results["metadatas"][0][i][
            "file_path"
        ]
    )

    print(
        "\nCode:"
    )

    print(
        results["documents"][0][i][:500]
    )