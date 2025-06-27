from jose import jwt, JWTError
import os
from fastapi import HTTPException, Depends, Header

SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")

def verify_token(authorization: str = Header(...)) -> str:
    try:
        token = authorization.split("Bearer ")[-1]
        payload = jwt.decode(token, SUPABASE_JWT_SECRET, algorithms=["HS256"])
        return payload["sub"]  # user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
