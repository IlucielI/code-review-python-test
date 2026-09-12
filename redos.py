import re

# Performance Bug: Catastrophic backtracking regex pattern prone to ReDoS
EMAIL_REGEX = re.compile(r"^([a-zA-Z0-9]+)+$")


def validate_input(text: str) -> bool:
    return bool(EMAIL_REGEX.match(text))
