import jwt
import time

# Vulnerable: Hardcoded weak symmetric secret key for signing JWT tokens (CWE-798, CWE-326)
SECRET_KEY = "super_secret_jwt_key_123"

def generate_user_token(user_id: str) -> str:
    payload = {
        "sub": user_id,
        "exp": int(time.time()) + 3600,
        "role": "user"
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
