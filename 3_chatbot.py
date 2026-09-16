# import all env variables
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini and get response
model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    # stream=True, for displaying the result
    response = chat.send_message(question, stream=True)
    return response

# initializing streamlit app
st.set_page_config(page_title="Q & A Demo")

st.header('Gemini LLM Application')

# initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)
    # add user query and response in the session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Response")

    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("The chat history is")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
