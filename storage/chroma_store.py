import chromadb

from shared.config import (
    CHROMA_DB_PATH,
    COLLECTION_NAME_PREFIX
)


_client = None


def get_client():

    global _client

    if _client is None:

        _client = chromadb.PersistentClient(
            path=CHROMA_DB_PATH
        )

    return _client


def get_collection(
    repo_slug: str
):

    client = get_client()

    collection_name = (
        f"{COLLECTION_NAME_PREFIX}"
        f"{repo_slug}"
    )

    collection = (
        client.get_or_create_collection(
            name=collection_name
        )
    )

    return collection
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
def search_chunks(
    collection,
    query_embedding,
    top_k=5
):

    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=top_k
    )

    return results