from fastapi import Response

# Insecure Cookie: setting authentication session cookie with httponly=False and secure=False
def set_session_cookie(response: Response, session_token: str):
    response.set_cookie(key="session_token", value=session_token, httponly=False, secure=False)
