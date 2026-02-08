import os
import json
from openai import OpenAI

# Folders
input_folder = r"C:\PyProjects\My_project\MockupCVs_JSON"   # JSONs with raw_text
output_folder = r"C:\PyProjects\My_project\MockupCVs_Final"  # Structured JSON output
os.makedirs(output_folder, exist_ok=True)

# --- Process each JSON file ---
for file in os.listdir(input_folder):
    if file.lower().endswith(".json"):
        input_path = os.path.join(input_folder, file)

        # Read raw_text from JSON
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        raw_text = data.get("raw_text", "")

        # --- Prompt for AI ---
        prompt = f"""
You are a professional resume parser. Extract all relevant information from the resume text below
and return it in valid JSON format exactly like this structure:

{{
  "personal_info": {{
    "name": "",
    "email": "",
    "phone": "",
    "location": ""
  }},
  "summary": "",
  "skills": [],
  "experience": [
    {{"title": "", "company": "", "start_date": "", "end_date": "", "description": ""}}
  ],
  "education": [
    {{"degree": "", "field": "", "institution": "", "year": ""}}
  ]
}}

Resume text:
{raw_text}

Extract all information you can. Keep the JSON valid.
"""

        # --- Call OpenAI API ---
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        # --- Get structured JSON ---
        structured_json = response.choices[0].message.content

        # --- Save output dynamically ---
        base_name = os.path.splitext(file)[0]
        output_path = os.path.join(output_folder, f"{base_name}_structured.json")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(structured_json)

        print(f"Processed: {file} → {base_name}_structured.json")