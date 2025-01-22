import nltk
import random
from nltk.chat.util import Chat, reflections
import streamlit as st

# Define a basic knowledge base
knowledge_base = {
    "algorithm": [
        "An algorithm is a step-by-step procedure for solving a problem.",
        "It's a set of instructions that a computer can follow to achieve a specific task.",
        "For example, a sorting algorithm arranges a list of items in a specific order."
    ],
    "python_for_loop": [
        "A for loop in Python is used to iterate over a sequence (like a list, tuple, or string).",
        "Example:",
        """
        ```python
        for i in range(5):
            print(i)
        ```
        """
    ],
    "sql": [
        "SQL stands for Structured Query Language.",
        "It's a language used to manage and manipulate data in relational databases."
    ],
    "java_interface_abstract": [
        "An interface in Java is a blueprint for a class, defining methods that a class must implement.",
        "An abstract class in Java is a class that cannot be instantiated and may contain abstract methods (methods without implementation).",
        "The main difference is that a class can implement multiple interfaces but can only inherit from one abstract class."
    ],
    "default": [
        "I'm not sure I understand. Can you rephrase?",
        "Could you please elaborate?",
        "I'm still learning, can you ask something else?"
    ]
}

# Define patterns and responses
pairs = [
    [
        r"what is an algorithm\??",
        knowledge_base["algorithm"]
    ],
    [
        r"show me an example of a for loop in python\??",
        knowledge_base["python_for_loop"]
    ],
    [
        r"what is sql\??",
        knowledge_base["sql"]
    ],
    [
        r"what is the difference between an interface and an abstract class in java\??",
        knowledge_base["java_interface_abstract"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!", "See you later!",]
    ],
    [
        r"(.*)",
        knowledge_base["default"]
    ],
]

# Create the chatbot
def chatbot(user_input):
    chat = Chat(pairs, reflections)
    response = chat.respond(user_input)
    return response

# Streamlit UI
st.title("Educational Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get chatbot response
    response = chatbot(prompt)
    # Add chatbot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    # Display chatbot response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
