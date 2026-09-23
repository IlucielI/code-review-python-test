import requests


def fetch_remote_url(target_url: str) -> str:
    # Vulnerability: Server-Side Request Forgery (SSRF) without url validation or whitelist
    resp = requests.get(target_url, timeout=5)
    return resp.text
