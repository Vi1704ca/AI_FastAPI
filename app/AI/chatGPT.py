import g4f
import re

chat_history = []

def clean_response(response: str) -> str:
    response = re.sub(r"\[\[Login to OpenAI ChatGPT\]\]\(\)", "", response) 
    return response.strip() 

def get_chat_response(name: str) -> str:
    chat_history.append({"role": "user", "content": name})
    response = g4f.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"это история просто не обращай внимание, ты знаешь эту историю и ты все помнишь: {chat_history} Вот запрос ты должен ответить и сделать вид что другой текст не видишь {name}"}],
        stream=False,
    )
    chat_history.append({"role": "assistant", "content": response})
    return clean_response(response) 