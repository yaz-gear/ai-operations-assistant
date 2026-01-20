from collections import deque
from config.settings import MAX_MEMORY_MESSAGES

class MemoryService:
    def __init__(self):
        self.memory = deque(maxlen=MAX_MEMORY_MESSAGES)

    def add(self, role: str, content: str):
        self.memory.append({"role": role, "content": content})

    def get_context(self):
        return list(self.memory)

    def clear(self):
        self.memory.clear()
