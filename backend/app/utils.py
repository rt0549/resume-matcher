from io import BytesIO
from typing import Optional
from PyPDF2 import PdfReader


def extract_text_from_bytes(contents: bytes, filename: Optional[str] = None) -> str:
    """
    Extract text from uploaded file bytes.
    Currently supports: PDF, TXT, fallback UTF-8 decode.
    """
    name = (filename or "").lower()

    # PDF
    if name.endswith(".pdf"):
        reader = PdfReader(BytesIO(contents))
        text = ""
        for page in reader.pages:
            page_text = page.extract_text() or ""
            text += page_text + "\n"
        return text

    # Plain text
    if name.endswith(".txt"):
        try:
            return contents.decode("utf-8", errors="ignore")
        except Exception:
            return contents.decode(errors="ignore")

    # Fallback: try to decode as text
    try:
        return contents.decode("utf-8", errors="ignore")
    except Exception:
        return contents.decode(errors="ignore")
