import pdfplumber
import json
from pathlib import Path

def pdf_to_json(pdf_path: str, output_path: str):
    data = {
        "file": Path(pdf_path).name,
        "pages": []
    }

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            data["pages"].append({
                "page": i,
                "text": text.strip()
            })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    pdf_to_json("input.pdf", "output.json")
