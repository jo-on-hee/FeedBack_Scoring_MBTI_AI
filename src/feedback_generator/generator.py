"""
Feedback Generator Module

This module is responsible for generating high-quality feedback based on manager's input.
"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

class FeedbackGenerator:
    """
    Generates improved feedback based on manager's original feedback
    """
    
    def __init__(self, model_name="gpt-4o", temperature=0.2):
        """
        Initialize the feedback generator
        
        Args:
            model_name: The OpenAI model to use
            temperature: Creativity level (0-1)
        """
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)
        self.prompt = PromptTemplate.from_template(
            """
            You are an expert feedback coach that helps managers provide better feedback to their team members.
            
            # Original Feedback from Manager:
            {original_feedback}
            
            # Context:
            {context}
            
            Please generate an improved version of this feedback that is:
            1. Specific and actionable
            2. Balanced (both positive aspects and areas for improvement)
            3. Growth-oriented
            4. Clear and concise
            5. Empathetic
            
            Provide only the improved feedback without any explanations or meta-commentary.
            """
        )
        
    def generate_feedback(self, original_feedback, context):
        """
        Generate improved feedback
        
        Args:
            original_feedback: The original feedback provided by the manager
            context: Additional context about the situation
            
        Returns:
            Improved feedback text
        """
        chain = (
            self.prompt 
            | self.llm 
            | StrOutputParser()
        )
        
        return chain.invoke({
            "original_feedback": original_feedback,
            "context": context
        })
