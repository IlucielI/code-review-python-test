import base64
import pickle


def deserialize_session(payload: str):
    # Vulnerability: Insecure deserialization via pickle.loads enables Remote Code Execution (RCE)
    raw = base64.b64decode(payload)
    data = pickle.loads(raw)
    return data
