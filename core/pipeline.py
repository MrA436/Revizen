from core.extractor import extract_text_from_pdf
from core.ai import generate_notes
import json, re

def summarize_pipeline(pdf_path):

    #extracting text from pdf
    text = extract_text_from_pdf(pdf_path)   
    result = revision_pipeline(text)
    return result

def parse_json(raw: str) -> dict:
    #fix wreird json
    clean = re.sub(r"```json|```", "", raw).strip()
    return json.loads(clean)

def revision_pipeline(text):
    stored = generate_notes(text)
    data = parse_json(stored)
    return data