def route_command(text: str) -> str:
    text = text.lower()

    if text.startswith("/help"):
        return "HELP"
    if text.startswith("/role"):
        return "ROLE"
    if text.startswith("/clear"):
        return "CLEAR"
    return "QUERY"
