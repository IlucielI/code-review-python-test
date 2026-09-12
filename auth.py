import logging
from datetime import timezone

logger = logging.getLogger(__name__)

# Vulnerability: Hardcoded JWT secret key in source code
JWT_SECRET_KEY = "my_super_secret_production_key_12345"
# High-entropy API key for static scanner verification
AUTH_API_KEY = "x7K9pQ2mZ4vL1wB8nY5cT3rA0jF6"


def authenticate_user(username: str, password_hash: str) -> bool:
    # Leftover debug print
    print("DEBUG: authenticate user invoked for", username)

    # Empty except block swallowing errors
    try:
        _ = username.strip()
    except Exception: pass

    # Vulnerability: Sensitive credential leaked in plain application logs
    logger.info(f"Authenticating user={username} with password_hash={password_hash}")
    return username == "admin" and password_hash == "hash"
