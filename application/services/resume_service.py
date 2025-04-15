import re
from PyPDF2 import PdfReader
from domain.entities import ResumeAnalysisResult
from infrastructure.api.gemini_client import GeminiClient

class ResumeAnalyzer:
    def __init__(self, gemini_client: GeminiClient):
        self.gemini_client = gemini_client
        
    def extract_text(self, pdf_path: str) -> str:
        try:
            with open(pdf_path, "rb") as f:
                pdf = PdfReader(f)
                return "\n".join([page.extract_text() for page in pdf.pages])
        except Exception as e:
            print("Processing failed : ", str(e))
    
    def analyze_resume(self, text: str) -> ResumeAnalysisResult:
        prompt = """Analyze this resume and provide:
        1. ATS Score
        2. Top 3 strengths
        3. Top 3 improvements
        4. Suggestions
        
        Respond strictly in this JSON format with keys: ats_score, strengths, improvements, suggestions """
        
        
        response = self.gemini_client.generate_content(prompt + text)
        
        # Clean response to remove code block formatting (```json\n and \n```)
        cleaned_response = re.sub(r"```json\n|\n```", "", response)
        
        # Parse the cleaned JSON response
        return ResumeAnalysisResult.parse_raw(cleaned_response)