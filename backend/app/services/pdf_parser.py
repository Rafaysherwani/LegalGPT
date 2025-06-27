from langchain.document_loaders import PyMuPDFLoader
import tempfile
from typing import List

def extract_text_from_pdf(file_bytes: bytes) -> List[str]:
    # Save to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name

    # Load using LangChain's PyMuPDFLoader
    loader = PyMuPDFLoader(tmp_path)
    docs = loader.load()

    return [doc.page_content for doc in docs]


