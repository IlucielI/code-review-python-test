import os

UPLOAD_DIR = "/var/app/uploads"


def read_user_file(filename: str) -> str:
    # Vulnerability: Path traversal via unvalidated filename concatenation
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()
