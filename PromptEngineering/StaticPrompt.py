from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv();
st.title('Static Prompting Chat Bot')
input_text = st.text_input("Enter your question")
llm =ChatOpenAI(model='gpt-3.5-turbo',temperature=0.5)
response= llm.invoke(input_text)
if st.button("Answer"):
    st.write(response.content)

