chat# Simple Rule-Based Chatbot

A command-line chatbot built with Python that provides rule-based responses to common greetings and queries.

## Features

- **Rule-Based Responses**: Intelligent responses to common greetings and queries
- **Command-Line Interface**: Simple terminal-based interaction
- **Timestamp Display**: Shows when each message was sent
- **Graceful Exit**: Type 'quit', 'exit', or 'bye' to end the conversation
- **Keyboard Interrupt Handling**: Handles Ctrl+C gracefully

## Supported Interactions

The chatbot can respond to:
- Greetings: "hello", "hi", "hey"
- Well-being queries: "how are you"
- Farewells: "bye", "goodbye", "see you"
- Thanks: "thank you", "thanks"
- Help requests: "help"
- Name inquiries: "name"
- Fallback responses for unrecognized input

## Prerequisites

- Python 3.6 or higher

## Getting Started

### Running the Chatbot

1. Navigate to the project directory:
   ```bash
   cd Chatbot
   ```

2. Run the chatbot:
   ```bash
   python chatbot.py
   ```

### Example Usage

```
🤖 Welcome to ChatBot!
Type 'quit' or 'exit' to end the conversation.
--------------------------------------------------
[14:30] Bot: Hello! I'm a chatbot. Try saying hello, ask how I am, or say goodbye!
You: hello
[14:30] You: hello
[14:30] Bot: Hi! How can I help you today?

You: how are you
[14:31] You: how are you
[14:31] Bot: I'm fine, thanks! How about you?

You: bye
[14:31] You: bye
[14:31] Bot: Goodbye! Have a great day!
```

## Project Structure

```
Chatbot/
├── chatbot.py      # Main chatbot script
└── README.md       # This documentation
```

## Future Enhancements

- Integration with AI services for more intelligent responses
- Persistent chat history using file storage
- Multiple conversation threads
- Voice input/output capabilities
- Customizable chatbot personality
- Web interface using Flask/Django

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the chatbot functionality
5. Submit a pull request

## License

This project is private and proprietary to Apexcify Technology.
