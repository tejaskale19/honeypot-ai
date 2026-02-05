import re
from typing import Dict


SCAM_KEYWORDS = [
    "otp",
    "one time password",
    "urgent",
    "immediately",
    "account blocked",
    "verify now",
    "click link",
    "kyc",
    "suspend",
    "bank",
    "upi",
    "payment",
    "refund"
]


def detect_scam(message: str) -> Dict:
    """
    Detect scam intent from message text.
    Returns:
        {
            is_scam: bool,
            confidence: float,
            category: str
        }
    """
    message_lower = message.lower()
    score = 0

    for keyword in SCAM_KEYWORDS:
        if keyword in message_lower:
            score += 1

    confidence = min(score / len(SCAM_KEYWORDS), 1.0)

    if score >= 2:
        return {
            "is_scam": True,
            "confidence": round(confidence, 2),
            "category": "financial_fraud"
        }

    return {
        "is_scam": False,
        "confidence": round(confidence, 2),
        "category": "unknown"
    }
