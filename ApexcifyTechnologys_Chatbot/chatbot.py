#!/usr/bin/env python3
"""
Simple Rule-Based Chatbot
A command-line chatbot that responds to basic greetings and queries.
"""

import datetime

def get_bot_response(user_input: str) -> str:
    """
    Generate a response based on user input using simple rule-based logic.

    Args:
        user_input (str): The user's message

    Returns:
        str: The bot's response
    """
    lower_input = user_input.lower().strip()

    if any(word in lower_input for word in ['hello', 'hi', 'hey']):
        return "Hi! How can I help you today?"
    elif any(phrase in lower_input for phrase in ['how are you', 'how are u']):
        return "I'm fine, thanks! How about you?"
    elif any(word in lower_input for word in ['bye', 'goodbye', 'see you']):
        return "Goodbye! Have a great day!"
    elif 'thank' in lower_input or 'thanks' in lower_input:
        return "You're welcome!"
    elif 'help' in lower_input:
        return "I can respond to greetings, check how you're doing, and say goodbye. Just try saying 'hello', 'how are you', or 'bye'!"
    elif 'name' in lower_input:
        return "I'm ChatBot, a simple rule-based chatbot!"
    else:
        return "I'm not sure how to respond to that. Try saying 'hello', 'how are you', or 'bye'!"

def print_message(sender: str, message: str, timestamp: datetime.datetime):
    """
    Print a formatted message with timestamp.

    Args:
        sender (str): 'User' or 'Bot'
        message (str): The message content
        timestamp (datetime.datetime): When the message was sent
    """
    time_str = timestamp.strftime("%H:%M")
    print(f"[{time_str}] {sender}: {message}")

def main():
    """Main function to run the chatbot."""
    print("🤖 Welcome to ChatBot!")
    print("Type 'quit' or 'exit' to end the conversation.")
    print("-" * 50)

    # Initial bot greeting
    initial_time = datetime.datetime.now()
    print_message("Bot", "Hello! I'm a chatbot. Try saying hello, ask how I am, or say goodbye!", initial_time)

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                farewell_time = datetime.datetime.now()
                print_message("Bot", "Goodbye! Have a great day!", farewell_time)
                break

            if not user_input:
                continue

            # Print user message
            user_time = datetime.datetime.now()
            print_message("You", user_input, user_time)

            # Get and print bot response
            bot_response = get_bot_response(user_input)
            bot_time = datetime.datetime.now()
            print_message("Bot", bot_response, bot_time)
            print()  # Empty line for readability

        except KeyboardInterrupt:
            print("\n🤖 ChatBot: Goodbye! Have a great day!")
            break
        except EOFError:
            break

if __name__ == "__main__":
    main()
