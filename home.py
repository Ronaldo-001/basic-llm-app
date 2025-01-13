import streamlit as st

st.title("Welcome to my first LLM request Application")

st.header("OpenAI LLM")
open_ai_prompt = st.text_input("Please enter your prompt")

if st.button("Send"):  #add button "Send" 
    #--
    st.success("Content Generated Succesfully!") # if success 
else:
    st.warning("Please insert a prompt!!")

st.divider()


st.header("Gemini LLM")
gemini_ai_prompt = st.text_input("Please enter your prompt" , key="gemini-input") # key differentiates the prompt from openai
st.text_input("Please select number of tokens")

if st.button("Send", key="gemini-button"):  #key differentiates the send button from openai
    #--
    st.success("Content Generated Succesfully!") # if success 
else:
    st.warning("Please insert a prompt!!")