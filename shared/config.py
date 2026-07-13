import re

EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"
EMBEDDING_DIM = 384

CHROMA_DB_PATH = "./data/chroma"

COLLECTION_NAME_PREFIX = "codeinsight_"


def repo_slug(repo_url: str) -> str:
    """
    Convert GitHub URL into a filesystem-safe repo name.

    Example:
    https://github.com/psf/requests
    -> requests
    """

    repo_name = repo_url.rstrip("/").split("/")[-1]

    repo_name = re.sub(r"[^a-zA-Z0-9_-]", "_", repo_name)

    return repo_name.lower()