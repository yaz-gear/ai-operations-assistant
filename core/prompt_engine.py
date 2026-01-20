from config.settings import SUPPORTED_ROLES

def system_prompt(role: str) -> str:
    role_desc = SUPPORTED_ROLES.get(role, "")
    return f"""
You are an AI Operations Assistant.

Role:
{role} – {role_desc}

Rules:
- Be professional
- Be structured
- Avoid speculation
- Use bullet points when helpful
"""

def user_prompt(context: str, user_input: str) -> str:
    return f"""
Context:
{context}

User Request:
{user_input}

Respond accordingly.
"""
