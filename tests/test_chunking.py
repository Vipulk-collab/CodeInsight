import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from parser.ast_parser import parse_python_file
from chunking.chunk_builder import create_chunk

file_path = (
    "data/repos/requests/src/requests/api.py"
)

nodes = parse_python_file(file_path)

chunk = create_chunk(
    nodes[0],
    file_path
)

for key, value in chunk.items():

    if key == "code_text":
        print(key)
        print(value[:300])

    else:
        print(key, value)