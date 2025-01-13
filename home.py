import streamlit as st
from gpt_wrapper import generate_content, generate_image
from gemini_wrapper import generate_text_gemini

# Set the title of the web application
st.title("Welcome to my first LLM request Application")

# Add a header for the OpenAI LLM section
st.header("OpenAI LLM")

# Input field for the OpenAI prompt
open_ai_prompt = st.text_input("Please enter your prompt")

# Button to send the OpenAI prompt
if st.button("Send"):  
    if open_ai_prompt:
        generate_content(open_ai_prompt)
        st.success("Content Generated Successfully!")  # Display success message
    else:
        st.warning("Please insert a prompt!!")  # Display warning if no prompt is entered

# Add a horizontal divider
st.divider()

# Add a header for the Gemini LLM section
st.header("Gemini LLM")

# Input field for the Gemini prompt with a unique key
gemini_ai_prompt = st.text_input("Please enter your prompt", key="gemini-input")

# Number input for the number of tokens with a range from 0 to 1000
gemini_tokens = st.number_input("Please enter your tokens", min_value=0, max_value=1000)

# Button to send the Gemini prompt with a unique key
if st.button("Send", key="gemini-button"):
    if gemini_ai_prompt:
        generate_text_gemini(gemini_ai_prompt, gemini_tokens)
        st.success("Content Generated Successfully!")  # Display success message
    else:
        st.warning("Please insert a prompt!!")  # Display warning if no prompt is entered

# Add some styling to make the webpage look nicer
st.markdown("""
    <style>
    .stButton button {
        background-color: #FF69B4;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px; 
    }
    .stTextInput input {
        border: 2px solid #FF69B4;
        border-radius: 4px;
        padding: 8px;
    }
    .stNumberInput input {
        border: 2px solid #FF69B4;
        border-radius: 4px;
        padding: 8px;
    }
    </style>
""", unsafe_allow_html=True)