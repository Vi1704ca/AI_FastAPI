import openai

TOKEN_API = "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"

openai.api_key = TOKEN_API
openai.api_base = "https://openrouter.ai/api/v1"

def get_ai_response(name: str) -> str:
    """Запрашивает ответ у модели DeepSeek через OpenRouter."""
    try:
        completion = openai.ChatCompletion.create(
            model="deepseek/deepseek-chat-v3-0324:free",
            messages=[{"role": "user", "content": name}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Ошибка: {str(e)}"