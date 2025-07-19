import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash-latest")  

def translate_text(input_text: str, target_language: str) -> str:
    prompt = f"""You are a professional language translator.
Translate the following sentence to {target_language}:

"{input_text}"

Only return the translated version — no explanation."""
    
    response = model.generate_content(prompt)
    return response.text.strip()