import os
import subprocess


def ping_host(host: str) -> str:
    # Vulnerability: Command injection via os.system with untrusted host
    os.system(f"ping -c 1 {host}")
    return "ping executed"


def run_diagnostics(command: str) -> str:
    # Vulnerability: Command injection via subprocess with shell=True
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, _ = proc.communicate()
    return stdout.decode()
