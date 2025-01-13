#This file is used to serve our gpt connection

#import dependencies
from openai import OpenAI
from streamlit as st

api_key= st.secrets["api_key"]    #import api from streamlit secrets
client = OpenAI(api_key=api_key)  #adding api key from openai
completion = client.chat.completions.create(    #function call to openai (arguments-model-messages)
    model="gpt-4o-mini",          #model to use 
    #store=True,
    messages=[
        {"role": "user", "content": "write about life"} # specify user and their prompt in content
    ]
)
print(completion.choices[0].message.content) # here the respose from gpt is in json so we use . format to access the answer