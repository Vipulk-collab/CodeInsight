from ingestion.github_loader import (
    clone_repo,
    get_python_files
)

repo_path = clone_repo(
    "https://github.com/psf/requests",
    "data/repos/requests"
)

files = get_python_files(repo_path)

print(f"Found {len(files)} Python files")

for file in files[:10]:
    print(file)