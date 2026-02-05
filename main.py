from fastapi import FastAPI, Header, HTTPException
from typing import Optional

from config import settings
from schemas import HoneypotRequest, HoneypotResponse
from scam_detector import detect_scam
from agent import HoneypotAgent
from extractor import extract_intel

app = FastAPI(title=settings.APP_NAME)

# Create agent once
agent = HoneypotAgent()


@app.get("/health")
def health_check():
    return {"status": "ok", "app": settings.APP_NAME}


@app.post("/honeypot", response_model=HoneypotResponse)
def honeypot_endpoint(
    request: HoneypotRequest,
    x_api_key: Optional[str] = Header(None)
):
    # 1️⃣ API key check
    if x_api_key != settings.HONEYPOT_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # 2️⃣ Scam detection
    detection = detect_scam(request.message)

    # 3️⃣ Agent reply
    reply_text = agent.generate_reply(detection, request.message)

    # 4️⃣ Extract intelligence
    intel_data = extract_intel(request.message)

    # 5️⃣ Hackathon-friendly tuning:
    # If any intelligence is found, treat as scam
    if (
        intel_data["urls"]
        or intel_data["upi_ids"]
        or intel_data["phone_numbers"]
        or intel_data["emails"]
    ):
        detection["is_scam"] = True

    # 6️⃣ Return response (THIS MUST BE INSIDE FUNCTION)
    return HoneypotResponse(
        reply=reply_text,
        is_scam=detection["is_scam"],
        confidence=detection["confidence"],
        intel=intel_data
    )
