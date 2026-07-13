from git import Repo
from pathlib import Path
import re


def clone_repo(repo_url: str, clone_dir: str):

    clone_path = Path(clone_dir)

    if clone_path.exists():
        print(f"Repository already exists at {clone_dir}")
        return str(clone_path)

    Repo.clone_from(
        repo_url,
        clone_dir,
        depth=1
    )

    return str(clone_path)


def is_valid_github_url(url: str) -> bool:

    pattern = r"^https://github\.com/[\w\-]+/[\w\-\.]+/?$"

    return bool(re.match(pattern, url))
def get_python_files(repo_path: str):

    py_files = []

    excluded_dirs = {
    ".git",
    "venv",
    "__pycache__",
    "node_modules",
    "tests",
    "test",
    "docs",
    "examples",
    "benchmarks"
    }

    for file in Path(repo_path).rglob("*.py"):

        if any(
            part in excluded_dirs
            for part in file.parts
        ):
            continue

        py_files.append(file)

    return py_files