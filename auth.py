import logging

logger = logging.getLogger(__name__)

# Vulnerability: Hardcoded JWT secret key in source code
JWT_SECRET_KEY = "my_super_secret_production_key_12345"


def authenticate_user(username: str, password_hash: str) -> bool:
    # Vulnerability: Sensitive credential leaked in plain application logs
    logger.info(f"Authenticating user={username} with password_hash={password_hash}")
    return username == "admin" and password_hash == "hash"
