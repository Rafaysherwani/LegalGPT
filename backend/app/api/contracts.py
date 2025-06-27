from fastapi import APIRouter, UploadFile, File, Header, HTTPException
from app.services.pdf_parser import extract_text_from_pdf
from app.services.genai import explain_contract
from app.services.supabase import save_contract_metadata
from app.utils.auth import verify_token

router = APIRouter()

@router.post("/analyze-contract")
async def analyze_contract(
    file: UploadFile = File(...),
    authorization: str = Header(...),  # Swagger can provide this
):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid header format")

    token = authorization.split("Bearer ")[-1]
    user_payload = verify_token(token)  # This should return user info like user_id
 # update this call

    # Read PDF, extract info
    file_bytes = await file.read()
    pages = extract_text_from_pdf(file_bytes)
    explanation = explain_contract("\n".join(pages))

    # Save metadata
    save_contract_metadata(user_id, file.filename, token)

    return {
        "pages": pages,
        "explanation": explanation
    }

