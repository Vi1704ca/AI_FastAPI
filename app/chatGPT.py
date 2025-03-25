import g4f
import re

def clean_response(response: str) -> str:
    response = re.sub(r"\[\[Login to OpenAI ChatGPT\]\]\(\)", "", response) 
    return response.strip() 

def get_chat_response(name: str) -> str:
    response = g4f.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"{name}"}],
        stream=False,
    )
    return clean_response(response) 