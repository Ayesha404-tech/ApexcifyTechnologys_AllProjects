#!/usr/bin/env python3
"""
Python Web-Based Chatbot using Streamlit
A modern web interface for the rule-based chatbot.
"""

import streamlit as st
import datetime
from datetime import datetime as dt

# Page configuration
st.set_page_config(
    page_title="ChatBot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
    }
    .user-message {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 12px;
        align-items: center;
    }
    .bot-message {
        display: flex;
        justify-content: flex-start;
        margin-bottom: 12px;
        align-items: center;
    }
    .message-bubble {
        padding: 12px 16px;
        border-radius: 12px;
        min-width: 60px;
        max-width: 80%;
        word-wrap: break-word;
        word-break: break-word;
        white-space: normal;
        font-size: 15px;
        line-height: 1.5;
        display: inline-block;
    }
    .user-bubble {
        background-color: #2563eb;
        color: white;
        border-radius: 12px 12px 0 12px;
    }
    .bot-bubble {
        background-color: #e2e8f0;
        color: #1e293b;
        border-radius: 12px 12px 12px 0;
    }
    .timestamp {
        font-size: 12px;
        color: #94a3b8;
        margin-top: 6px;
        text-align: center;
    }
    .header {
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
        color: white;
        padding: 24px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
    }
    .header h1 {
        margin: 0;
        font-size: 32px;
        font-weight: 700;
    }
    .header p {
        margin: 8px 0 0 0;
        font-size: 15px;
        opacity: 0.95;
    }
    .stTextInput > div > div > input {
        font-size: 15px !important;
        padding: 12px 16px !important;
    }
    .stButton > button, .stFormSubmitButton > button {
        font-size: 16px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        width: 100% !important;
        height: auto !important;
    }
    </style>
""", unsafe_allow_html=True)


def get_bot_response(user_input: str) -> str:
    """
    Generate a response based on user input using simple rule-based logic.

    Args:
        user_input (str): The user's message

    Returns:
        str: The bot's response
    """
    lower_input = user_input.lower().strip()

    # Greetings
    if any(word in lower_input for word in ['hello', 'hi', 'hey', 'hii', 'hiiii']):
        responses = [
            "Hi! How can I help you today?",
            "Hello! Great to see you! 😊",
            "Hey there! What's up?",
            "Hi! How are you doing?",
        ]
        import random
        return random.choice(responses)
    
    # How are you
    elif any(phrase in lower_input for phrase in ['how are you', 'how are u', "how's it", "how are things"]):
        responses = [
            "I'm doing great, thanks for asking! How about you?",
            "I'm feeling awesome! 😄 How are you?",
            "All good! Just here to help you out. You good?",
            "Fantastic! Ready to assist you!",
        ]
        import random
        return random.choice(responses)
    
    # Goodbye
    elif any(word in lower_input for word in ['bye', 'goodbye', 'see you', 'farewell', 'adios', 'cya']):
        responses = [
            "Goodbye! Have a great day! 👋",
            "See you later! Take care!",
            "Bye! Come back soon! 😊",
            "Farewell! Hope I was helpful!",
        ]
        import random
        return random.choice(responses)
    
    # Thanks/Thank you
    elif 'thank' in lower_input or 'thanks' in lower_input:
        responses = [
            "You're welcome! Happy to help! 😊",
            "My pleasure! Anytime!",
            "You're very welcome!",
            "No problem at all!",
        ]
        import random
        return random.choice(responses)
    
    # Help
    elif 'help' in lower_input:
        return "I can help you with:\n• Greetings (say 'hello', 'hi', 'hey')\n• Check my mood (ask 'how are you')\n• Farewell (say 'bye', 'goodbye')\n• Thank me (say 'thanks')\n• Know about me (ask 'what is your name')\n• Get this help again (say 'help')\n\nTry any of these! 😊"
    
    # Name/Who are you
    elif any(word in lower_input for word in ['name', 'who are you', 'what are you', "who's this", 'introduce']):
        responses = [
            "I'm ChatBot, a simple rule-based chatbot! Nice to meet you! 🤖",
            "You can call me ChatBot! I'm here to chat with you! 😊",
            "I'm ChatBot - your friendly assistant!",
            "Hello! I'm ChatBot, created to help and chat with you!",
        ]
        import random
        return random.choice(responses)
    
    # What time is it
    elif any(phrase in lower_input for phrase in ['time', 'what time', "what's the time"]):
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"Current time is: {current_time} ⏰"
    
    # How to use
    elif any(phrase in lower_input for phrase in ['how to', 'how do i', 'how can i']):
        return "Just type any message and I'll respond! You can greet me, ask how I'm doing, say goodbye, or ask for help. Go ahead and try! 😊"
    
    # Nice/Good
    elif any(word in lower_input for word in ['nice', 'good', 'great', 'awesome', 'cool']):
        responses = [
            "Glad you think so! 😊",
            "Thanks! That's kind of you to say!",
            "I appreciate that! Keep smiling! 🌟",
            "Happy to please you!",
        ]
        import random
        return random.choice(responses)
    
    # Feelings/How are you feeling
    elif any(phrase in lower_input for phrase in ['feeling', 'mood', 'how am i', 'i feel']):
        responses = [
            "I hope you're feeling good! If not, I'm here to chat! 😊",
            "That's great to know! Keep up the positive vibes!",
            "Remember, every day is a new opportunity!",
            "I'm here if you need someone to talk to!",
        ]
        import random
        return random.choice(responses)
    
    # Yes/No
    elif lower_input in ['yes', 'yeah', 'yep', 'yup', 'si', 'sure']:
        responses = [
            "Awesome! 🎉",
            "Great choice!",
            "Perfect! 😊",
            "I agree!",
        ]
        import random
        return random.choice(responses)
    
    elif lower_input in ['no', 'nope', 'nah']:
        responses = [
            "No problem! 😊",
            "That's alright!",
            "Okay, understood!",
            "No worries!",
        ]
        import random
        return random.choice(responses)
    
    # Confused/Questions
    elif any(word in lower_input for word in ['what', 'why', 'when', 'where', 'who', '?']):
        return "That's a good question! I'm a simple chatbot, so I might not have all the answers. But feel free to ask me anything! 😊"
    
    # Default response
    else:
        responses = [
            "That's interesting! Tell me more! 😊",
            "I'm not sure I understand that completely, but I'm learning! 🤖",
            "Cool! Anything else you'd like to chat about?",
            "Interesting input! Try saying 'help' to see what I can do!",
            "That sounds interesting! 😊",
        ]
        import random
        return random.choice(responses)


# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "text": "Hello! I'm a chatbot. Try saying hello, ask how I am, or say goodbye!",
            "sender": "bot",
            "timestamp": dt.now()
        }
    ]

# Header
st.markdown("""
    <div class="header">
        <h1>🤖 ChatBot</h1>
        <p>Simple Rule-Based Assistant</p>
    </div>
""", unsafe_allow_html=True)

# Chat history display
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if message["sender"] == "user":
            st.markdown(f"""
                <div class="user-message">
                    <div>
                        <div class="message-bubble user-bubble">
                            {message['text']}
                        </div>
                        <div class="timestamp">{message['timestamp'].strftime('%H:%M')}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="bot-message">
                    <div>
                        <div class="message-bubble bot-bubble">
                            {message['text']}
                        </div>
                        <div class="timestamp">{message['timestamp'].strftime('%H:%M')}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# Input section
st.markdown("---")

# Create input form to handle Enter key
with st.form(key="chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1], gap="small")
    
    with col1:
        user_input = st.text_input(
            label="",
            placeholder="Type your message here...",
            label_visibility="collapsed"
        )
    
    with col2:
        send_button = st.form_submit_button("📤 Send", use_container_width=True)

# Handle message sending
if send_button and user_input.strip():
    # Add user message
    st.session_state.messages.append({
        "text": user_input,
        "sender": "user",
        "timestamp": dt.now()
    })
    
    # Get bot response
    bot_response = get_bot_response(user_input)
    st.session_state.messages.append({
        "text": bot_response,
        "sender": "bot",
        "timestamp": dt.now()
    })
    
    # Clear input and rerun
    st.rerun()

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #94a3b8; font-size: 12px;">
        <p>Powered by Streamlit | Simple Rule-Based Chatbot</p>
    </div>
""", unsafe_allow_html=True)
