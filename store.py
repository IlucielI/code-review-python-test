import sqlite3


def get_user_by_username(username: str):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # Vulnerability: Raw SQL injection via direct f-string concatenation
    query = f"SELECT id, username, role FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result
