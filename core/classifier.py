def classify_task(text: str) -> str:
    keywords = {
        "analysis": ["analyze", "compare", "evaluate", "assess"],
        "summary": ["summarize", "brief", "short"],
        "decision": ["recommend", "decide", "should"],
    }

    for category, keys in keywords.items():
        for key in keys:
            if key in text.lower():
                return category

    return "general"
