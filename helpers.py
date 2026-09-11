def add_tag(tag: str, tags: list = []) -> list:
    # Syntax / Logic Bug: Mutable default argument retains state across function invocations
    tags.append(tag)
    return tags
