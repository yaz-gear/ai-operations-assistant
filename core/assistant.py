from core.prompt_engine import build_prompt, BASE_SYSTEM_PROMPT
from core.command_router import route_command
from services.openai_service import call_llm

class AIAssistant:

    def handle_request(self, user_input: str) -> str:
        command = route_command(user_input)

        if command == "HELP":
            return self.help_message()

        context = self.build_context(command)
        prompt = build_prompt(context, user_input)

        return call_llm(BASE_SYSTEM_PROMPT, prompt)

    def build_context(self, command: str) -> str:
        if command == "ANALYZE":
            return "The user wants analytical reasoning or structured analysis."

        if command == "SUMMARY":
            return "The user wants a concise professional summary."

        return "General operational assistance."

    def help_message(self) -> str:
        return """
Available Commands:
/help       - Show available commands
/analyze    - Request structured analysis
/summary    - Request a concise summary

Example:
/analyze Improve warehouse process efficiency
"""
