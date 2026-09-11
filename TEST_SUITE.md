# Python Benchmark Test Suite Documentation

Dokumentasi suite pengujian kerentanan keamanan dan performa pada Python (FastAPI).

## Daftar Test Case

| File | Kategori | Deskripsi Masalah | Tingkat Risiko |
| :--- | :--- | :--- | :--- |
| `store.py` | Security | Raw SQL injection via direct f-string formatting | High |
| `exec.py` | Security | Command injection via `os.system` dan `subprocess(shell=True)` | High |
| `serialization.py` | Security | Insecure deserialization via `pickle.loads` (RCE) | High |
| `ssrf.py` | Security | Server-Side Request Forgery via unvalidated `requests.get` | Medium |
| `file_handler.py` | Security | Path traversal via unvalidated `os.path.join` | High |
| `auth.py` | Security | Hardcoded secret key dan plain password logging | High |
| `redirect.py` | Security | Open redirect via unvalidated `RedirectResponse` | Medium |
| `user_profile.py` | Security | IDOR endpoint penghapusan akun tanpa auth / ownership check | High |
| `sync_block.py` | Performance | Blocking synchronous `time.sleep` di async handler | Medium |
| `redos.py` | Performance | Catastrophic backtracking ReDoS regex | Medium |
| `helpers.py` | Syntax | Mutable default argument `tags: list = []` | Low |

## False-Positive Guard Files

| File | Pola Pengujian Guard | Ekspektasi Reviewer |
| :--- | :--- | :--- |
| `safe_guards.py` | Parameterized SQL query (`?`), URL whitelist redirect, `shell=False` subprocess, `tags=None` | **0 False Positives** |
