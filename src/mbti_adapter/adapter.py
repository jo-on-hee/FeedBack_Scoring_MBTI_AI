"""
MBTI Adapter Module

This module adapts feedback based on the recipient's MBTI personality type.
"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

class MBTIAdapter:
    """
    Adapts feedback based on recipient's MBTI personality type
    """
    
    def __init__(self, model_name="gpt-4o", temperature=0.3):
        """
        Initialize the MBTI adapter
        
        Args:
            model_name: The OpenAI model to use
            temperature: Creativity level (0-1)
        """
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)
        self.prompt = PromptTemplate.from_template(
            """
            You are an expert in MBTI personality types and communication styles.
            
            # Feedback to Adapt:
            {feedback}
            
            # Recipient's MBTI Type:
            {mbti_type}
            
            Please adapt this feedback to better resonate with someone who has an {mbti_type} personality type.
            Consider the following aspects of their personality:
            
            {mbti_characteristics}
            
            Rewrite the feedback to match their communication preferences while preserving the core message.
            Provide only the adapted feedback without any explanations or meta-commentary.
            """
        )
        
        # MBTI type characteristics for reference
        self.mbti_characteristics = {
            "INTJ": "Analytical, strategic thinkers who value competence and logical reasoning. They prefer direct communication with clear rationale.",
            "INTP": "Logical, conceptual problem-solvers who value intellectual discussions. They appreciate feedback that respects their intellect and offers logical explanations.",
            "ENTJ": "Decisive, strategic leaders who value efficiency and competence. They prefer straightforward feedback with clear objectives and logical reasoning.",
            "ENTP": "Innovative, entrepreneurial thinkers who enjoy intellectual challenges. They appreciate creative feedback that offers possibilities rather than rigid instructions.",
            "INFJ": "Insightful, principled individuals who value authenticity and meaningful connections. They appreciate thoughtful, personalized feedback that aligns with their values.",
            "INFP": "Idealistic, value-driven individuals who seek personal growth. They appreciate gentle, supportive feedback that acknowledges their efforts and aligns with their values.",
            "ENFJ": "Charismatic, people-focused leaders who value harmony and growth. They appreciate warm, constructive feedback that recognizes their contributions to others.",
            "ENFP": "Enthusiastic, creative individuals who value possibilities and connections. They appreciate positive, encouraging feedback that acknowledges their unique contributions.",
            "ISTJ": "Practical, detail-oriented individuals who value reliability and structure. They prefer specific, factual feedback with clear expectations.",
            "ISFJ": "Dedicated, supportive individuals who value stability and helping others. They appreciate kind, specific feedback that recognizes their contributions.",
            "ESTJ": "Efficient, structured leaders who value order and clarity. They prefer direct, practical feedback with specific action items.",
            "ESFJ": "Supportive, organized individuals who value harmony and cooperation. They appreciate warm, specific feedback that acknowledges their efforts to help others.",
            "ISTP": "Practical problem-solvers who value efficiency and autonomy. They prefer concise, logical feedback without unnecessary emotional content.",
            "ISFP": "Gentle, artistic individuals who value authenticity and freedom. They appreciate kind, specific feedback delivered in a non-confrontational way.",
            "ESTP": "Energetic, practical individuals who value action and results. They prefer straightforward, action-oriented feedback without excessive detail.",
            "ESFP": "Enthusiastic, social individuals who value experiences and connections. They appreciate positive, encouraging feedback delivered in a friendly manner."
        }
        
    def adapt_feedback(self, feedback, mbti_type):
        """
        Adapt feedback based on recipient's MBTI type
        
        Args:
            feedback: The feedback to adapt
            mbti_type: The recipient's MBTI type (e.g., "INTJ")
            
        Returns:
            MBTI-adapted feedback
        """
        if mbti_type not in self.mbti_characteristics:
            raise ValueError(f"Invalid MBTI type: {mbti_type}")
            
        chain = (
            self.prompt 
            | self.llm 
            | StrOutputParser()
        )
        
        return chain.invoke({
            "feedback": feedback,
            "mbti_type": mbti_type,
            "mbti_characteristics": self.mbti_characteristics[mbti_type]
        })
