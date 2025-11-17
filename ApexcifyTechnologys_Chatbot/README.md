# Simple Rule-Based Chatbot 🤖

A versatile chatbot built with Python that provides intelligent rule-based responses. Now available in both **command-line** and **modern web interface** versions using Streamlit!

## 🌟 Features

### Core Features
- **Rule-Based Responses**: Smart responses to 10+ different categories of input
- **Multiple Response Variations**: Random responses to avoid repetition
- **Timestamp Display**: Shows when each message was sent
- **Graceful Exit**: Multiple ways to end the conversation
- **Keyboard Interrupt Handling**: Handles Ctrl+C gracefully

### Web Version Features (Streamlit) ✨
- **Modern Web Interface**: Beautiful gradient UI with message bubbles
- **Real-time Chat**: Send messages with Enter key or Send button
- **Chat History**: Persistent conversation display
- **Responsive Design**: Works on desktop and mobile devices
- **User-Friendly**: Clean and intuitive interface

## 🎯 Supported Interactions

The chatbot can intelligently respond to:
- **Greetings**: "hello", "hi", "hey", "hii"
- **Well-being**: "how are you", "how are u", "how's it"
- **Farewells**: "bye", "goodbye", "see you", "adios", "cya"
- **Gratitude**: "thank you", "thanks"
- **Help**: "help" (shows available commands)
- **About Bot**: "what's your name", "who are you", "introduce yourself"
- **Time**: "what time is it", "current time"
- **Yes/No**: "yes", "yeah", "no", "nope"
- **Feelings**: "how am i feeling", "mood", "feeling"
- **Feedback**: "nice", "good", "great", "awesome", "cool"
- **Questions**: General question handling with smart fallback responses

## 📋 Prerequisites

- **Python 3.7 or higher**
- **pip** (Python package manager)

## 🚀 Installation

1. Clone or navigate to the project directory:
   ```bash
   cd ApexcifyTechnologys_Chatbot
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Running the Chatbot

### Option 1: Web Version (Recommended) 🌐

Start the modern web interface:
```bash
streamlit run chatbot_web.py
```

The chatbot will open in your browser at: **http://localhost:8501**

**Features:**
- Beautiful gradient blue interface
- Real-time message bubbles
- Send with Enter key or Send button
- Full conversation history

### Option 2: Command-Line Version

Run the classic terminal version:
```bash
python chatbot.py
```

**Features:**
- Simple terminal-based interaction
- Timestamped messages
- Type 'quit' or 'exit' to end

## 📁 Project Structure

```
ApexcifyTechnologys_Chatbot/
├── chatbot_web.py          # Streamlit web app (Main)
├── chatbot.py              # Command-line version
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── config.toml        # Streamlit configuration
└── README.md              # This file
```

## 📦 Dependencies

- **streamlit** (1.51.0+) - For the web interface
- **datetime** - Built-in Python module

## 🎨 Customization

### Add More Responses

Edit the `get_bot_response()` function in `chatbot_web.py` to add more response categories:

```python
elif any(word in lower_input for word in ['your_keyword']):
    responses = [
        "Response 1",
        "Response 2",
    ]
    import random
    return random.choice(responses)
```

### Modify UI Colors

Update the CSS in the `st.markdown()` section to change colors:
- User messages: `#2563eb` (blue)
- Bot messages: `#e2e8f0` (light gray)
- Header: `#2563eb` to `#1e40af` (blue gradient)

## 🤖 Example Interactions

```
User: Hello
Bot: Hey there! What's up?

User: How are you?
Bot: I'm feeling awesome! 😄 How are you?

User: What's your name?
Bot: I'm ChatBot, a simple rule-based chatbot! Nice to meet you! 🤖

User: Help
Bot: I can help you with:
     • Greetings (say 'hello', 'hi', 'hey')
     • Check my mood (ask 'how are you')
     • ... and more!
```

## 📝 Notes

- The web version uses Streamlit's session state to maintain conversation history
- Each message includes a timestamp in HH:MM format
- The chatbot provides random responses from a pool to avoid repetition
- All responses are case-insensitive

## 🛠️ Troubleshooting

### Streamlit not found
```bash
pip install streamlit
```

### Port 8501 already in use
```bash
streamlit run chatbot_web.py --server.port 8502
```

### Email prompt appearing
The `.streamlit/config.toml` file disables analytics and email prompts automatically.

## 📄 License

This project is open source and available for educational and commercial use.

## 👤 Author

Created by **Apexcify Technologies**

## 🙏 Support

For issues or suggestions, please create an issue in the repository.
