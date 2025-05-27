"""
Feedback Scoring Engine

This module evaluates and scores feedback based on predefined criteria.
"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Dict, List

class FeedbackScore(BaseModel):
    """Schema for feedback scoring results"""
    specificity: int = Field(description="Score for how specific and actionable the feedback is (1-10)")
    balance: int = Field(description="Score for balance between positive aspects and areas for improvement (1-10)")
    growth_orientation: int = Field(description="Score for focus on growth and development (1-10)")
    clarity: int = Field(description="Score for clarity and conciseness (1-10)")
    empathy: int = Field(description="Score for empathy and consideration of recipient's feelings (1-10)")
    overall: int = Field(description="Overall score (1-10)")
    strengths: List[str] = Field(description="List of feedback strengths")
    improvement_areas: List[str] = Field(description="List of areas for improvement")

class FeedbackScorer:
    """
    Scores feedback quality based on predefined criteria
    """
    
    def __init__(self, model_name="gpt-4o", temperature=0):
        """
        Initialize the feedback scorer
        
        Args:
            model_name: The OpenAI model to use
            temperature: Creativity level (0-1)
        """
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)
        self.prompt = PromptTemplate.from_template(
            """
            You are an expert feedback coach that evaluates the quality of feedback.
            
            # Feedback to Evaluate:
            {feedback}
            
            Please evaluate this feedback based on the following criteria:
            1. Specificity: How specific and actionable is the feedback? (1-10)
            2. Balance: Does it balance positive aspects with areas for improvement? (1-10)
            3. Growth Orientation: Does it focus on growth and development? (1-10)
            4. Clarity: Is it clear and concise? (1-10)
            5. Empathy: Does it show empathy and consideration for the recipient's feelings? (1-10)
            
            Also calculate an overall score (1-10) based on these criteria.
            
            Identify the main strengths of this feedback and areas for improvement.
            
            Format your response as a JSON object with the following structure:
            {
                "specificity": <score>,
                "balance": <score>,
                "growth_orientation": <score>,
                "clarity": <score>,
                "empathy": <score>,
                "overall": <score>,
                "strengths": ["strength1", "strength2", ...],
                "improvement_areas": ["area1", "area2", ...]
            }
            """
        )
        self.parser = JsonOutputParser(pydantic_object=FeedbackScore)
        
    def score_feedback(self, feedback):
        """
        Score the quality of feedback
        
        Args:
            feedback: The feedback to evaluate
            
        Returns:
            Dictionary with scores and evaluation
        """
        chain = (
            self.prompt 
            | self.llm 
            | self.parser
        )
        
        return chain.invoke({"feedback": feedback})
