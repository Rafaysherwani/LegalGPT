import os
from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
#supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

def save_contract_metadata(user_id: str, filename: str, access_token: str):
    user_supabase = create_client(
        SUPABASE_URL,
        SUPABASE_SERVICE_KEY,
        options={"global": {"headers": {"Authorization": f"Bearer {access_token}"}}}
    )

    data = {
        "user_id": user_id,
        "file_name": filename,
    }

    user_supabase.table("contracts").insert(data).execute()
