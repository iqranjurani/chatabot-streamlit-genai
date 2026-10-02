
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv(".env")

# Streamlit page setup
st.set_page_config(
    page_title="💬 ChatBot",
    page_icon="🤖",
    layout="wide",
)

st.title("💬 InsightIQ")

# Initialize Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Add user message to chat history
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    # Invoke LLM
    response = llm.invoke(
        [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            *st.session_state.chat_history
        ]
    )

    # Extract assistant response
    assistant_response = response.content

    # Add assistant response to chat history
    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
