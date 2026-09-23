import yaml
from typing import List, Optional

# Safe: uses SafeLoader to prevent code execution
def parse_configuration_safe(content: str) -> dict:
    return yaml.safe_load(content)

# Safe: default is None, initialized inside function
def append_to_audit_log_safe(entry: str, log_list: Optional[List[str]] = None) -> List[str]:
    if log_list is None:
        log_list = []
    log_list.append(entry)
    return log_list
