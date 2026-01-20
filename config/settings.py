import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0.3
MAX_TOKENS = 600

MAX_MEMORY_MESSAGES = 6

LOG_FILE = "assistant.log"

DEFAULT_ROLE = "operations"

SUPPORTED_ROLES = {
    "analyst": "Analytical, structured, data-focused",
    "operations": "Practical, actionable, process-driven",
    "executive": "Concise, strategic, decision-oriented"
}
