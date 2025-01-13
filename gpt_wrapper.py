#This file is used to serve our gpt connection

#import dependencies
from openai import OpenAI
import streamlit as st
import requests

api_key= st.secrets["api_key"]    #import api from streamlit secrets
client = OpenAI(api_key=api_key)  #adding api key from openai

def generate_content(prompt):
    completion = client.chat.completions.create(    #function call to openai (arguments-model-messages)
        model="gpt-4o-mini",          #model to use 
        #store=True,
        messages=[
            {"role": "user", "content": prompt} # specify user and their prompt in content
        ]
    )
    # return completion.choices[0].message.content # here the respose from gpt is in json so we use . format to access the answer
    st.write(completion.choices[0].message.content) # write output in streamlit page

def generate_image(prompt):
    response = client.images.generate(  #calling image gen function with prompts
        model="dall-e-3",               #parameters of the function
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,  #quantity of images
    )
    #print(response.data[0].url) #url link to download generated image
    image_url= (response.data[0].url) 

    image_response = requests.get(image_url) # use requests lib to downlaod image using api request

    with open("images/new.png", 'wb') as file: #name the downloaded file and save to local path
        file.write(image_response.content)  # calling file write function to save