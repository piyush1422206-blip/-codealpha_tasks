# ==========================================
# Rule-Based Chatbot
# Internship Project
# ==========================================

def chatbot_response(user_input):
    """
    Returns a response based on the user's input.
    """

    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! Nice to meet you."

    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How can I help you?"

    elif user_input in ["what is your name", "what is your name?"]:
        return "I'm a simple Python-based chatbot."

    elif user_input in ["help", "help me"]:
        return "I can respond to greetings, basic questions, and goodbye."

    elif user_input in ["thank you", "thanks"]:
        return "You're welcome!"

    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that. Please try another question."


def start_chatbot():
    """
    Starts and manages the chatbot conversation.
    """

    print("=" * 45)
    print("        WELCOME TO PYTHON CHATBOT")
    print("=" * 45)

    print("Type 'bye' or 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        # Check for empty input
        if not user_input.strip():
            print("Bot: Please enter something.")
            continue

        response = chatbot_response(user_input)

        print("Bot:", response)

        # Stop chatbot when user says goodbye
        if user_input.lower().strip() in [
            "bye",
            "goodbye",
            "exit",
            "quit"
        ]:
            break


# Program starts here
if __name__ == "__main__":
    start_chatbot()
