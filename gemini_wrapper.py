import google.generativeai as genai
import streamlit as st

api_key = st.secrets["api_key_google"] #access api key 



def generate_text_gemini(prompt,tokens):
    genai.configure(api_key= api_key) #use access key
    model = genai.GenerativeModel("gemini-1.5-flash")  #model used
    response = model.generate_content(  #function to call llm with arguments
        prompt, #prompt
        generation_config = genai.GenerationConfig( #config argument
        max_output_tokens=tokens, #max text
        temperature=0.1, #morality rate 
        )
    )
    #return response.text
    st.text(response.text)