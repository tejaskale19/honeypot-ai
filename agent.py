from typing import Dict
import random


class HoneypotAgent:
    """
    Rule-based autonomous honeypot agent.
    Designed to sound human and extract scam intelligence.
    """

    def __init__(self):
        self.bait_questions = [
            "I am not able to see the details clearly. Can you please share the exact link?",
            "Which bank is this related to? I have multiple accounts.",
            "The payment app is asking for UPI ID. Can you confirm it?",
            "Is this related to my savings or current account?",
            "I clicked something earlier, can you resend the link?"
        ]

        self.safe_responses = [
            "Okay, please give me a moment.",
            "I am checking this now.",
            "Just a second, the app is loading.",
            "I am not very technical, please explain."
        ]

    def generate_reply(self, detection: Dict, message: str) -> str:
        """
        Generate next honeypot reply based on scam detection.
        """

        # If scam detected → engage & extract
        if detection.get("is_scam"):
            return random.choice(self.bait_questions)

        # If not scam → neutral response
        return random.choice(self.safe_responses)
