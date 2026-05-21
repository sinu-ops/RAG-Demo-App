import os
import time
from google import genai
from google.genai.errors import ServerError

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_text(prompt, retries=3, delay=2):
    for attempt in range(retries):
        try:
            chat = client.chats.create(model="gemini-1.5-flash")
            response = chat.send_message(prompt)
            return response.text
        except ServerError as e:
            if attempt < retries - 1:
                time.sleep(delay * (attempt + 1))
                continue
            return "⚠️ Gemini is overloaded (503). Please try again in a minute."