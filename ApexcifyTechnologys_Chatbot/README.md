# Simple Rule-Based Chatbot 🤖

A versatile chatbot built with Python that provides intelligent rule-based responses. Now available in both **command-line** and **modern web interface** versions using Streamlit!

## 🌟 Features

### Core Features
- ✅ **Rule-Based Responses**: Smart responses to 15+ different categories of input
- ✅ **Multiple Response Variations**: Random responses to avoid repetition
- ✅ **Timestamp Display**: Shows when each message was sent
- ✅ **Graceful Exit**: Multiple ways to end the conversation
- ✅ **Keyboard Interrupt Handling**: Handles Ctrl+C gracefully

### Web Version Features (Streamlit) ✨
- 🎨 **Modern Web Interface**: Beautiful gradient blue UI with message bubbles
- ⚡ **Real-time Chat**: Send messages with Enter key or Send button
- 💬 **Chat History**: Persistent conversation display with timestamps
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🎯 **User-Friendly**: Clean and intuitive interface with emoji support

## 🎯 Supported Interactions

The chatbot can intelligently respond to:
- **Greetings**: "hello", "hi", "hey", "hii", "hiiii"
- **Well-being**: "how are you", "how are u", "how's it", "how are things"
- **Farewells**: "bye", "goodbye", "see you", "adios", "cya", "farewell"
- **Gratitude**: "thank you", "thanks"
- **Help**: "help" (shows available commands)
- **About Bot**: "what's your name", "who are you", "introduce yourself"
- **Time**: "what time is it", "current time"
- **Yes/No**: "yes", "yeah", "no", "nope", "nah"
- **Feelings**: "how am i feeling", "mood", "feeling"
- **Feedback**: "nice", "good", "great", "awesome", "cool"
- **Questions**: "what", "why", "when", "where", "who", "?"

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

## 💻 Usage

### Option 1: Web Version (Recommended) 🌐

```bash
python -m streamlit run chatbot_web.py
```

Open browser at: **http://localhost:8501**

### Option 2: Command-Line Version 🖥️

```bash
python chatbot.py
```

## 🎨 Features Highlight

- Beautiful gradient blue interface
- Real-time message bubbles
- Send with Enter key or button
- Full conversation history
- Emoji support

## 📦 Dependencies

- streamlit (1.51.0+)
- Python built-in modules

## 📝 Example

```
User: Hello
Bot: Hi! How can I help you today?

User: What's your name?
Bot: I'm ChatBot - your friendly assistant! 🤖
```

## 🐛 Troubleshooting

Port already in use:
```bash
streamlit run chatbot_web.py --server.port 8502
```

## 📄 License

Open source project by Apexcify Technologies

## 👤 Author

**Ayesha404-tech** - https://github.com/Ayesha404-tech

---

**Last Updated**: November 18, 2024 | **Version**: 2.0
