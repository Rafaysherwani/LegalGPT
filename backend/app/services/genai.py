import openai
from app.core.config import OPENROUTER_API_KEY

openai.api_key = OPENROUTER_API_KEY
openai.api_base = "https://openrouter.ai/api/v1"

def explain_contract(text: str) -> str:
    prompt = f"""You are a legal assistant AI. Explain the following contract in simple language for a non-lawyer:

{text}

Please break it into understandable sections."""
    
    response = openai.ChatCompletion.create(
        model="qwen/qwen3-30b-a3b:free",  # You can change to "mistral", "claude", etc.
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    
    return response.choices[0].message["content"]
