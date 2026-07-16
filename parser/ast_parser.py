import ast


def parse_python_file(file_path: str):

    with open(file_path, "r", encoding="utf-8") as f:
        source_code = f.read()

    tree = ast.parse(source_code)

    parsed_nodes = []

    for node in tree.body:

        if isinstance(
            node,
            ast.ClassDef
        ):

            parsed_nodes.append(
                {
                    "name": node.name,
                    "class_name": None,
                    "type": "ClassDef",

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

            for child in node.body:

                if isinstance(
                    child,
                    (
                        ast.FunctionDef,
                        ast.AsyncFunctionDef
                    )
                ):

                    parsed_nodes.append(
                        {
                            "name":
                            child.name,

                            "class_name":
                            node.name,

                            "type":
                            type(child).__name__,

                            "docstring":
                            ast.get_docstring(
                                child
                            ),

                            "source_code":
                            ast.get_source_segment(
                                source_code,
                                child
                            ),

                            "start_line":
                            child.lineno,

                            "end_line":
                            getattr(
                                child,
                                "end_lineno",
                                child.lineno
                            )
                        }
                    )

        elif isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef
            )
        ):

            parsed_nodes.append(
                {
                    "name":
                    node.name,

                    "class_name":
                    None,

                    "type":
                    type(node).__name__,

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