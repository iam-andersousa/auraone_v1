import os
import json

# --- Folders ---
input_folder = r"C:\PyProjects\My_project\MockupCVs_JSON"   # JSONs with raw_text
output_folder = r"C:\PyProjects\My_project\MockupCVs_Final"  # Structured JSON output
os.makedirs(output_folder, exist_ok=True)

# --- Template for structured JSON ---
def create_empty_structure(raw_text=""):
    return {
        "personal_info": {
            "name": "",
            "email": "",
            "phone": "",
            "location": ""
        },
        "summary": "",
        "skills": [],
        "experience": [
            {"title": "", "company": "", "start_date": "", "end_date": "", "description": ""}
        ],
        "education": [
            {"degree": "", "field": "", "institution": "", "year": ""}
        ],
        "raw_text": raw_text  # keep original text for reference
    }

# --- Process each JSON file ---
for file in os.listdir(input_folder):
    if file.lower().endswith(".json"):
        input_path = os.path.join(input_folder, file)

        # Read raw_text from JSON
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        raw_text = data.get("raw_text", "")

        # Create structured JSON using template
        structured_json = create_empty_structure(raw_text)

        # Save output dynamically
        base_name = os.path.splitext(file)[0]
        output_path = os.path.join(output_folder, f"{base_name}_structured.json")

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(structured_json, f, ensure_ascii=False, indent=2)

        print(f"Processed: {file} → {base_name}_structured.json")
