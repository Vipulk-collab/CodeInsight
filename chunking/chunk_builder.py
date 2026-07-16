import hashlib
from pathlib import Path


def generate_chunk_id(
    file_path: str,
    function_name: str,
    start_line: int
):
    unique_string = (
        f"{file_path}_"
        f"{function_name}_"
        f"{start_line}"
    )

    return hashlib.md5(
        unique_string.encode()
    ).hexdigest()


def create_chunk(
    parsed_node,
    file_path,
    repo_root
):
    relative_path = str(
        Path(file_path).relative_to(
            Path(repo_root)
        )
    )

    docstring = parsed_node.get(
        "docstring",
        ""
    )

    if docstring:
        code_text = (
            docstring
            + "\n\n"
            + parsed_node["source_code"]
        )
    else:
        code_text = (
            parsed_node["source_code"]
        )

    return {

        "id": generate_chunk_id(
            file_path,
            parsed_node["name"],
            parsed_node["start_line"]
        ),

        "code_text": code_text,

        "file_path": relative_path,

        "function_name": parsed_node["name"],

        "class_name":
        parsed_node.get(
            "class_name"
        ),
        

        "language": "python",

        "start_line": parsed_node["start_line"],

        "end_line": parsed_node["end_line"]
    }


def create_chunks_from_nodes(
    parsed_nodes,
    file_path,
    repo_root
):
    chunks = []

    for node in parsed_nodes:

        chunk = create_chunk(
            node,
            str(file_path),
            str(repo_root)
        )

        chunks.append(chunk)

    return chunks