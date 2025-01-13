#This file is used to serve our gpt connection

api_key="api-xxx"
from openai import OpenAI
client = OpenAI(api_key=api_key)  #adding api key from openai
completion = client.chat.completions.create(      #function call to openai (arguments-model-messages)
    model="gpt-4o-mini",     #nodel to use 
    #store=True,
    messages=[
        {"role": "user", "content": "write about life"} # specify user and their prompt in content
    ]
)
print(completion.choices[0].message.content) # here the respose from gpt is in json so we use . format to access the answer