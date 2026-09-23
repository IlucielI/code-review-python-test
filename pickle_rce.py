import pickle
import base64
from typing import Any

# Vulnerable: unpickling untrusted payload leads to Remote Code Execution (RCE)
def load_session_payload(raw_cookie: str) -> Any:
    binary_data = base64.b64decode(raw_cookie)
    return pickle.loads(binary_data) # BUG: RCE vulnerability via pickle deserialization
