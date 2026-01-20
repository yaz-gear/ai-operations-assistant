def format_response(task_type: str, content: str) -> str:
    if task_type == "analysis":
        return f"ANALYSIS\n\n{content}"

    if task_type == "summary":
        return f"SUMMARY\n\n{content}"

    if task_type == "decision":
        return f"RECOMMENDATION\n\n{content}"

    return content
