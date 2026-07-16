from pathlib import Path

from ingestion.github_loader import (
    clone_repo,
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

from shared.config import (
    repo_slug
)

from storage.chroma_store import (
    get_collection,
    upsert_chunks
)


def index_repository(
    repo_url: str
):

    repo_name = repo_slug(
        repo_url
    )

    repo_path = str(
        Path("data/repos")
        / repo_name
    )

    print(
        f"Cloning {repo_url}"
    )

    clone_repo(
        repo_url,
        repo_path
    )

    files = get_python_files(
        repo_path
    )

    all_chunks = []

    for file in files:

        try:

            nodes = parse_python_file(
                str(file)
            )

            chunks = (
                create_chunks_from_nodes(
                    nodes,
                    str(file),
                    repo_path
                )
            )

            all_chunks.extend(
                chunks
            )

        except Exception as e:

            print(
                f"Skipping {file}"
            )

            print(e)

    print(
        f"Chunks Created: {len(all_chunks)}"
    )

    texts = [

        chunk["code_text"]

        for chunk in all_chunks
    ]

    embeddings = encode_documents(
        texts
    )

    collection = get_collection(
        repo_name
    )

    upsert_chunks(
        collection,
        all_chunks,
        embeddings
    )

    print(
        f"Stored {len(all_chunks)} chunks"
    )

    return {
        "repo_name": repo_name,
        "files": len(files),
        "chunks": len(all_chunks)
    }