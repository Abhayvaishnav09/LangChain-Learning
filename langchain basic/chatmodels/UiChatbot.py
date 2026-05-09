# app.py

import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Load env variables
load_dotenv()

# Initialize model
model = init_chat_model(model="mistral-small-2506", temperature=0.9)

# Streamlit UI
st.set_page_config(page_title="Funny AI Chatbot", page_icon="🤖")

st.title("🤖 Funny AI Chatbot")
st.write("Type '0' to exit the conversation")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="you are a funny AI agent")
    ]

# Display previous chat (skip system message)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# Input box
prompt = st.chat_input("Type your message...")

if prompt:
    # Exit condition
    if prompt == "0":
        st.stop()

    # Add user message
    st.session_state.messages.append(HumanMessage(content=prompt))
    
    with st.chat_message("user"):
        st.write(prompt)

    # Get response
    response = model.invoke(st.session_state.messages)

    # Add AI response
    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(response.content)