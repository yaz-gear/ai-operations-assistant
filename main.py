from core.assistant import AIAssistant
from utils.validators import validate_input
from utils.logger import log

def main():
    assistant = AIAssistant()
    log("AI Operations Assistant started.")

    while True:
        user_input = input("\n> ")

        if user_input.lower() in ["exit", "quit"]:
            log("Session ended.")
            break

        if not validate_input(user_input):
            print("Invalid input.")
            continue

        response = assistant.handle_request(user_input)
        print("\nAssistant Response:\n")
        print(response)

if __name__ == "__main__":
    main()
