from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI   
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# LangSmith tracing
print("Tracing:", os.getenv("LANGSMITH_TRACING"))
print("Project:", os.getenv("LANGSMITH_PROJECT"))

os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGSMITH_PROJECT")

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system","I am a chatbot here to assist you. Please type your queries."),
    ("user","Question: {question}")
])

# Streamlit UI
st.title("LLM-Gemini PROJECT - CUSTOM LLM By Munna")

input_text = st.text_input("How may I help you?")

# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# Handle user input
if input_text:
    with st.spinner("🤔 Gemini 2.5 Flash is generating a response..."):
        try:
            response = chain.invoke({"question": input_text})
            st.success("✅ Here's my response:")
            st.write(response)
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")