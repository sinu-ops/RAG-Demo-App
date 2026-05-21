import os
from google import genai

# You can change this to another model from the Gemini models list
MODEL = "gemini-2.5-flash"

def generate_text(prompt: str) -> str:
    # API key is picked from GEMINI_API_KEY or GOOGLE_API_KEY env vars
    client = genai.Client()
    chat = client.chats.create(model=MODEL)
    response = chat.send_message(prompt)
    return response.text