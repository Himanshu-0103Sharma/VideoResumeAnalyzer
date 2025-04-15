from flask import jsonify, request
import tempfile
import os
from application.services.resume_service import ResumeAnalyzer
from infrastructure.api.gemini_client import GeminiClient

class ResumeController:
    def __init__(self):
        self.analyzer = ResumeAnalyzer(GeminiClient())
        
    def analyze(self):
        if 'resume' not in request.files:
            return jsonify({"error": "No resume uploaded"}), 400
        
        resume_file = request.files['resume']
        if not resume_file or resume_file.filename == '':
            return jsonify({"error": "Empty file received"}), 400
        
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as f:
                resume_path = f.name
                resume_file.save(resume_path)
                
                print("Extracting text from resume...")
                text = self.analyzer.extract_text(resume_path)
                
                print("Analysing resume...")
                analysis = self.analyzer.analyze_resume(text)
                
                return jsonify(analysis.dict()), 200
        
        except Exception as e:
            print("Error while analysing : ", str(e))
        
        
        finally:
            if os.path.exists(resume_path):
                os.remove(resume_path)