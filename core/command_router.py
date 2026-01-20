def route_command(user_input: str) -> str:
    user_input = user_input.lower()

    if user_input.startswith("/help"):
        return "HELP"

    if user_input.startswith("/analyze"):
        return "ANALYZE"

    if user_input.startswith("/summary"):
        return "SUMMARY"

    return "GENERAL"
