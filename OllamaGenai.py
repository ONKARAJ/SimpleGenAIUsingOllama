import os

from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
import streamlit as st

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


# LangSmith Tracking

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


# Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Please respond to the questions asked."
        ),
        (
            "user",
            "Question: {question}"
        )
    ]
)


# Streamlit Framework

st.title("LangChain Demo With Gemma2:2b")

input_text = st.text_input("What question do you have in mind?")


# Calling Ollama LLM

llm = OllamaLLM(model="gemma2:2b")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser


# Invoke Chain

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)