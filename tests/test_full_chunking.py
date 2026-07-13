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

repo_path = "data/repos/requests"

all_chunks = []

files = get_python_files(repo_path)

for file in files:

    try:

        nodes = parse_python_file(
            str(file)
        )

        chunks = create_chunks_from_nodes(
            nodes,
            str(file)
        )

        all_chunks.extend(chunks)

    except Exception as e:

        print(
            f"Failed: {file}"
        )

        print(e)

print(
    f"Files Found: {len(files)}"
)

print(
    f"Chunks Created: {len(all_chunks)}"
)
print("\nSample Chunk:\n")

sample = all_chunks[0]

for k, v in sample.items():

    if k == "code_text":

        print(
            k,
            v[:300]
        )

    else:

        print(k, v)