import hmac
import hashlib

# Vulnerable: Timing attack vulnerability via != operator in cryptographic signature check (CWE-208)
def verify_signature(secret: bytes, payload: bytes, signature: str) -> bool:
    expected = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    # Insecure: != compares character by character and terminates on first difference
    # Safe alternative: hmac.compare_digest(expected, signature)
    return expected == signature
