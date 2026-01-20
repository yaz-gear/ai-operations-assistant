from services.openai_service import call_llm
from services.memory_service import MemoryService
from services.logging_service import log_event
from core.prompt_engine import system_prompt, user_prompt
from core.classifier import classify_task
from core.formatter import format_response

class AIAssistant:
    def __init__(self, role: str):
        self.role = role
        self.memory = MemoryService()

    def handle(self, user_input: str) -> str:
        task_type = classify_task(user_input)
        log_event("USER_INPUT", user_input)

        messages = [{"role": "system", "content": system_prompt(self.role)}]
        messages.extend(self.memory.get_context())
        messages.append({"role": "user", "content": user_input})

        raw_response = call_llm(messages)
        formatted = format_response(task_type, raw_response)

        self.memory.add("user", user_input)
        self.memory.add("assistant", formatted)

        log_event("ASSISTANT_OUTPUT", formatted)
        return formatted

    def clear_memory(self):
        self.memory.clear()
