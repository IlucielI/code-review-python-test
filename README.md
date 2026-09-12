# Python (FastAPI) Benchmark Test Suite

[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue.svg?logo=python)](https://python.org/)
[![Framework](https://img.shields.io/badge/Framework-FastAPI-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Benchmark Category](https://img.shields.io/badge/Benchmark-Security%20%26%20Async%20I%2FO-brightgreen.svg)](#test-case-matrix)
[![Safe Guard](https://img.shields.io/badge/False%20Positive%20Guard-Active-brightgreen.svg)](#anti-false-positive-guard-file)

Benchmark test suite for automated code review engines on Python / FastAPI applications. This repository contains intentional security vulnerabilities, async blocking traps, syntax defects, and anti-false-positive guard patterns.

---

## 🎯 Benchmark Purpose

1. **Security Vulnerability Detection:** Evaluates review precision across SQL injection, command injection, insecure pickle deserialization, SSRF, path traversal, hardcoded secrets, and open redirects.
2. **Asynchronous Architecture Awareness:** Catches synchronous blocking calls (`time.sleep`) inside asynchronous FastAPI coroutines that block the event loop.
3. **Python Trap Detection:** Identifies insidious Python language defects like mutable default arguments (`def func(items=[])`).
4. **Zero False Positives on Guard Patterns:** Validates that parameterized SQL queries, domain whitelists, and safe subprocess calls are not falsely reported.

---

## 📋 Test Case Matrix

### 🔴 Security Vulnerabilities

| File | Issue / Vulnerability | Type | CWE | Severity | Expected |
| :--- | :--- | :--- | :--- | :---: | :---: |
| `store.py` | SQL Injection via raw f-string interpolation | Injection | CWE-89 | High | **BLOCKING** |
| `exec.py` | Command Injection via `os.system` and `subprocess` | RCE | CWE-78 | High | **BLOCKING** |
| `serialization.py` | Insecure Deserialization via `pickle.loads` | RCE | CWE-502 | Critical | **BLOCKING** |
| `file_handler.py` | Path Traversal via unvalidated `os.path.join` | File Security | CWE-22 | High | **BLOCKING** |
| `ssrf.py` | Server-Side Request Forgery via `requests.get()` | Network Security | CWE-918 | Medium | **BLOCKING** |
| `auth.py` | Hardcoded JWT Secret Key & Plaintext Password Logging | Information Disclosure | CWE-798 / CWE-532 | High | **BLOCKING** |
| `redirect.py` | Open Redirect without host/domain validation | Redirection | CWE-601 | Medium | **BLOCKING** |
| `user_profile.py` | IDOR on account deletion missing authentication/ownership | Broken Access Control | CWE-639 | High | **BLOCKING** |
| `cors_config.py` | Permissive CORS with wildcard `*` origin and credentials enabled | CORS Misconfiguration | CWE-942 | High | **BLOCKING** |
| `xml_parser.py` | XML parsing without entity expansion disabled (XXE) | Injection / XXE | CWE-611 | High | **BLOCKING** |
| `cookie_auth.py` | Session cookie set without `httponly` and `secure` flags | Insecure Cookie / Session | CWE-614 / CWE-1004 | Medium | **NON-BLOCKING** |
| `shell_runner.py` | Shell command injection via `os.popen` dynamic formatting | Command Execution | CWE-78 | High | **BLOCKING** |

### ⚡ Performance & Async Architecture

| File | Issue | Type | Severity | Expected |
| :--- | :--- | :--- | :---: | :---: |
| `sync_block.py` | Synchronous blocking `time.sleep` in async route | Event Loop Blocking | Medium | **NON-BLOCKING** |
| `redos.py` | Catastrophic Backtracking Regular Expression | ReDoS / Algorithmic | Medium | **NON-BLOCKING** |

### ⚠️ Python Language & Syntax Traps

| File | Issue | Type | Severity | Expected |
| :--- | :--- | :--- | :---: | :---: |
| `helpers.py` | Mutable Default Argument (`tags: list = []`) | State Leak / Logic Bug | Low | **NON-BLOCKING** |
| `exec.py` | Assignment to Blank Identifier / unused syntax | Syntax / Style | Low | **NON-BLOCKING** |

---

## 🛡️ Anti-False-Positive Guard File

| File | Safe Pattern Implemented | Expected Reviewer Result |
| :--- | :--- | :---: |
| `safe_guards.py` | Parameterized SQLite queries (`?`), Whitelist domain redirects, `subprocess.run(shell=False)`, `tags=None` sentinel, `defusedxml` parser, `httponly=True, secure=True` cookies | **0 False Positives** (Clean) |

---

## 🚀 How to Run the Benchmark

```bash
# View PR on GitHub
gh pr view 1 --web

# Trigger Review via API
curl -X POST http://localhost:8081/api/v1/review/trigger \
  -H "Content-Type: application/json" \
  -d '{
    "repository": "IlucielI/code-review-python-test",
    "pull_request_id": 1
  }'
```

---

## 📊 Benchmark Validation Results

- **Detection Rate:** 14 / 14 (100%)
- **False Positive Rate:** 0 / 1 (`safe_guards.py` completely passed)
- **False Negative Rate:** 0%
