import streamlit as st
import ollama

# Page configuration
st.set_page_config(
    page_title="AI Library Assistant",
    page_icon="📚"
)

st.title("📚 AI Library Assistant")
st.write("Ask me anything about books, libraries, programming, or computer science.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User question
user_input = st.chat_input("Ask your question...")

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # AI response
    try:
        response = ollama.chat(
            model="llama3.2",
            messages=st.session_state.messages
        )

        answer = response["message"]["content"]

        # Show AI response
        with st.chat_message("assistant"):
            st.write(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        st.error("Could not connect to Ollama.")
        st.write("Make sure Ollama is running and the llama3.2 model is installed.")
        st.code(str(e))