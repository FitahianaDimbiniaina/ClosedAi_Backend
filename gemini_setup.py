import logging
from dotenv import load_dotenv
import os
import google.generativeai as genai

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

try:
    load_dotenv()
    logging.info(".env file loaded successfully.")
except Exception as e:
    logging.error(f"Error loading .env file: {e}")

try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-pro")
except Exception as e:
    logging.error(f"Error configuring Gemini API: {e}")

def get_gemini_response(prompt, system_instruction=None):
    try:
        if system_instruction:
            response = model.generate_content(
                [system_instruction, prompt]
            )
        else:
            response = model.generate_content(prompt)

        logging.info(f"Gemini response: {response.text.strip()}")
        return response.text.strip()
    except Exception as e:
        logging.error(f"Error generating response from Gemini API: {e}")
        return "Sorry, I couldn't process your request at the moment."