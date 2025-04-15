from pydantic import BaseModel
from typing import List

class VideoAnalysisRequest(BaseModel): # Data required to send to the api
    video_path: str
    
class VideoAnalysisResult(BaseModel): # Data returned by the api
    transcript: str
    analysis: str
    metrics: dict = None
    
class ResumeAnalysisResult(BaseModel):
    ats_score: int
    strengths: List[str]
    improvements: List[str]
    suggestions: List[str]