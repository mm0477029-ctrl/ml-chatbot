import streamlit as st
from chatbot import EducationChatbot
import os

# Set page config
st.set_page_config(
    page_title="Education FAQ Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        width: 100%;
    }
    .user-message {
        background-color: #E3F2FD;
        justify-content: flex-end;
    }
    .bot-message {
        background-color: #F5F5F5;
        justify-content: flex-start;
    }
    .message-content {
        max-width: 80%;
        padding: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize chatbot
@st.cache_resource
def load_chatbot():
    return EducationChatbot('faq_data.json')

chatbot = load_chatbot()

# Sidebar
with st.sidebar:
    st.header("📚 About This Bot")
    st.write("""
    This is an Education FAQ Chatbot designed to help answer questions about:
    - **Courses** - Available programs and degrees
    - **Admission** - Requirements and process
    - **Fees** - Tuition, application, and hostel fees
    - **Scholarships** - Financial aid options
    """)
    
    st.divider()
    
    st.subheader("💡 Example Questions")
    examples = [
        "What courses are available?",
        "What are admission requirements?",
        "How much is the tuition fee?",
        "Are scholarships available?",
        "When is the admission deadline?"
    ]
    for example in examples:
        if st.button(example, key=example):
            st.session_state.user_input = example
    
    st.divider()
    st.caption("Made with ❤️ using Streamlit & ML")

# Main content
st.title("🤖 Education FAQ Chatbot")
st.markdown("Ask any questions about courses, admissions, or fees!")

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"""
            <div class="chat-message user-message">
                <div class="message-content">
                    <b>You:</b> {message["content"]}
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="chat-message bot-message">
                <div class="message-content">
                    <b>Bot:</b> {message["content"]}
                </div>
            </div>
            """, unsafe_allow_html=True)

# User input
st.divider()

col1, col2 = st.columns([5, 1])

with col1:
    user_input = st.text_input(
        "Your question:",
        value=st.session_state.user_input,
        placeholder="Type your question here...",
        key="input_field"
    )

with col2:
    send_button = st.button("Send", key="send_btn")

# Process user input
if send_button and user_input.strip():
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Get bot response
    bot_response = chatbot.get_response(user_input)
    
    # Add bot message to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })
    
    # Clear input
    st.session_state.user_input = ""
    
    # Rerun to display new messages
    st.rerun()

# Suggestions
if len(st.session_state.messages) > 0:
    st.divider()
    st.subheader("Suggested Questions:")
    
    suggestions = chatbot.get_suggestions("admission fees scholarship")
    cols = st.columns(len(suggestions) if suggestions else 1)
    
    for idx, suggestion in enumerate(suggestions):
        with cols[idx]:
            if st.button(suggestion, key=f"suggestion_{idx}"):
                st.session_state.user_input = suggestion
                st.rerun()
