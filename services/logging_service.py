from datetime import datetime
from config.settings import LOG_FILE

def log_event(event_type: str, content: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {event_type}: {content}\n")
