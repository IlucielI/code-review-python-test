import os

# Command injection via os.popen with unescaped user parameter
def run_diagnostic(param: str) -> str:
    stream = os.popen(f"ping -c 1 {param}")
    return stream.read()
