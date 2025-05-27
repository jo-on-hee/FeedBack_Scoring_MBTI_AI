"""
Main application for the Feedback Scoring MBTI AI project
"""
import os
from dotenv import load_dotenv
from src.feedback_generator.generator import FeedbackGenerator
from src.mbti_adapter.adapter import MBTIAdapter
from src.scoring_engine.scorer import FeedbackScorer
from src.config.settings import MBTI_TYPES

# Load environment variables
load_dotenv()

class FeedbackApp:
    """
    Main application for feedback generation, adaptation, and scoring
    """
    
    def __init__(self):
        """Initialize the feedback application components"""
        self.generator = FeedbackGenerator()
        self.adapter = MBTIAdapter()
        self.scorer = FeedbackScorer()
        
    def process_feedback(self, original_feedback, context, mbti_type):
        """
        Process feedback through the entire pipeline
        
        Args:
            original_feedback: Original feedback from manager
            context: Additional context about the situation
            mbti_type: MBTI type of the recipient
            
        Returns:
            Dictionary with original, improved, and adapted feedback along with scores
        """
        # Validate MBTI type
        if mbti_type not in MBTI_TYPES:
            raise ValueError(f"Invalid MBTI type: {mbti_type}. Must be one of {MBTI_TYPES}")
        
        # Generate improved feedback
        improved_feedback = self.generator.generate_feedback(original_feedback, context)
        
        # Adapt feedback to MBTI type
        adapted_feedback = self.adapter.adapt_feedback(improved_feedback, mbti_type)
        
        # Score the feedback
        original_score = self.scorer.score_feedback(original_feedback)
        improved_score = self.scorer.score_feedback(improved_feedback)
        adapted_score = self.scorer.score_feedback(adapted_feedback)
        
        return {
            "original": {
                "feedback": original_feedback,
                "score": original_score
            },
            "improved": {
                "feedback": improved_feedback,
                "score": improved_score
            },
            "adapted": {
                "feedback": adapted_feedback,
                "score": adapted_score,
                "mbti_type": mbti_type
            }
        }

def main():
    """Main function to demonstrate the feedback app"""
    app = FeedbackApp()
    
    # Example usage
    original_feedback = "You need to improve your communication skills."
    context = "The team member has been missing deadlines and not updating the team on progress."
    mbti_type = "INTJ"
    
    result = app.process_feedback(original_feedback, context, mbti_type)
    
    print("\n=== ORIGINAL FEEDBACK ===")
    print(result["original"]["feedback"])
    print(f"Overall Score: {result['original']['score']['overall']}/10")
    
    print("\n=== IMPROVED FEEDBACK ===")
    print(result["improved"]["feedback"])
    print(f"Overall Score: {result['improved']['score']['overall']}/10")
    
    print(f"\n=== ADAPTED FEEDBACK FOR {mbti_type} ===")
    print(result["adapted"]["feedback"])
    print(f"Overall Score: {result['adapted']['score']['overall']}/10")
    
if __name__ == "__main__":
    main()
