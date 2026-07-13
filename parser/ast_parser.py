import ast


def parse_python_file(file_path: str):

    with open(file_path, "r", encoding="utf-8") as f:
        source_code = f.read()

    tree = ast.parse(source_code)

    parsed_nodes = []

    for node in ast.walk(tree):

        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef
            )
        ):

            parsed_nodes.append(
                {
                    "name": node.name,
                    "type": type(node).__name__,

                    "docstring":
                    ast.get_docstring(node),

                    "source_code":
                    ast.get_source_segment(
                        source_code,
                        node
                    ),

                    "start_line":
                    node.lineno,

                    "end_line":
                    getattr(
                        node,
                        "end_lineno",
                        node.lineno
                    )
                }
            )

    return parsed_nodes