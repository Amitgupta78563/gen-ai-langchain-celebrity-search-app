## integrate our code OpenAI API
import os
# from langchain.llms import OpenAI/
from langchain_community.llms import OpenAI

import streamlit as st

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Example usage
print(f"Your OpenAI API key: {openai_api_key}")

# Use the API key securely in your application


# os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("search the topic u want")

##OPENAI LLMS

llm=OpenAI(temperature=0.8)


if input_text:
    st.write(llm(input_text))
