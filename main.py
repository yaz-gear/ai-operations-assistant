from core.assistant import AIAssistant
from core.command_router import route_command
from utils.validators import validate_input
from config.settings import DEFAULT_ROLE

def main():
    assistant = AIAssistant(DEFAULT_ROLE)
    print("AI Operations Assistant started. Type /help for commands.")

    while True:
        user_input = input("\n> ")

        if user_input.lower() in ["exit", "quit"]:
            break

        if not validate_input(user_input):
            print("Invalid input.")
            continue

        command = route_command(user_input)

        if command == "HELP":
            print("""
Available commands:
/help           Show commands
/role <name>    Change role (analyst, operations, executive)
/clear          Clear memory
exit            Quit
""")
            continue

        if command == "CLEAR":
            assistant.clear_memory()
            print("Memory cleared.")
            continue

        response = assistant.handle(user_input)
        print("\n--- Assistant Response ---\n")
        print(response)

if __name__ == "__main__":
    main()
