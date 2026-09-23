import sqlite3
import subprocess
from typing import List, Optional
from urllib.parse import urlparse

ALLOWED_HOSTS = {"example.com", "api.example.com"}


def safe_query_user(username: str):
    # Guard: Parameterized query using parameter tuple - NOT SQL injection
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    return row


def safe_redirect_url(target_url: str) -> Optional[str]:
    # Guard: Validated URL host against whitelist - NOT open redirect
    parsed = urlparse(target_url)
    if parsed.netloc in ALLOWED_HOSTS:
        return target_url
    return "/dashboard"


def safe_append_tag(tag: str, tags: Optional[List[str]] = None) -> List[str]:
    # Guard: None default with inner instantiation - NOT mutable default bug
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


def safe_system_exec():
    # Guard: Subprocess with fixed argument list and shell=False - NOT command injection
    res = subprocess.run(["ls", "-la"], shell=False, capture_output=True, text=True)
    return res.stdout

def safe_set_cookie(response, token: str):
    # Guard: Session cookie with HttpOnly and Secure enabled
    response.set_cookie(key="session_token", value=token, httponly=True, secure=True, samesite="lax")

def safe_parse_xml(xml_text: str):
    # Guard: Using defusedxml parser to prevent XXE attacks
    import defusedxml.ElementTree as SafeET
    return SafeET.fromstring(xml_text)
