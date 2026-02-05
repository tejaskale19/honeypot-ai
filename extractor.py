import re
from typing import Dict, List


def extract_intel(message: str) -> Dict[str, List[str]]:
    """
    Extract scam intelligence from message text.
    """

    phone_numbers = re.findall(r"\b\d{10}\b", message)
    urls = re.findall(r"https?://[^\s]+", message)
    upi_ids = re.findall(r"\b[\w.-]+@[\w.-]+\b", message)
    emails = re.findall(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", message)

    return {
        "phone_numbers": phone_numbers,
        "urls": urls,
        "upi_ids": upi_ids,
        "emails": emails
    }
