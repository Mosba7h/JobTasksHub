from openai import OpenAI
from config import OPENAI_API_KEY

# Instantiate new v1.x client
client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_text(text: str) -> str:
    """
    Summarize input text using ChatCompletion API.
    """
    if not text:
        return ""
    prompt = f"Please summarize the following text:\n{text[:3000]}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content