import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from parser.ast_parser import parse_python_file

file_path = "data/repos/requests/src/requests/api.py"

nodes = parse_python_file(file_path)

first = nodes[0]

print("Name:")
print(first["name"])

print("\nType:")
print(first["type"])

print("\nDocstring Preview:")
print(first["docstring"][:200])

print("\nSource Code Preview:")
print(first["source_code"][:500])