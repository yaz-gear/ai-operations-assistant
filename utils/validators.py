def validate_input(text: str) -> bool:
    if not text:
        return False
    if len(text.strip()) < 3:
        return False
    return True
