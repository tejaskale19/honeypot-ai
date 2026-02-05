from pydantic import BaseModel, Field
from typing import Optional, List


class HoneypotRequest(BaseModel):
    session_id: str = Field(..., description="Unique session or attacker ID")
    message: str = Field(..., description="Incoming message from attacker")
    source: Optional[str] = Field(
        default="unknown",
        description="Source channel (sms, whatsapp, email, web, etc.)"
    )


class ExtractedIntel(BaseModel):
    phone_numbers: List[str] = []
    urls: List[str] = []
    upi_ids: List[str] = []
    emails: List[str] = []


class HoneypotResponse(BaseModel):
    reply: str = Field(..., description="AI honeypot response")
    is_scam: bool = Field(..., description="Whether scam intent is detected")
    confidence: float = Field(
        ..., ge=0.0, le=1.0, description="Scam confidence score (0–1)"
    )
    intel: Optional[ExtractedIntel] = None
