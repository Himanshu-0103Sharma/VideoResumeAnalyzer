from core.config import settings
import google.generativeai as genai

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
    def generate_content(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text