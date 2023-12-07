# Q&A Chatbot
from langchain.llms import openai
from dotenv import load_dotenv

load_dotenv() # Take environment variables from .env

import streamlit as st
import os

#Function to load OpenAI model and get response

def get_openai_response(question):
    llm = openai.OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), 
                 model_name= 'text-davinci-003', 
                 temperature = 0.6)
    response = llm(question)
    return response

## Initialize our Streamlit Apps

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input: ",key='input')
response = get_openai_response(input)

submit = st.button("Ask the question")

if submit:
    st.subheader("The response is")
    st.write(response)

