import re
import openai
import fitz  # PyMuPDF
import docx

# OpenRouter.ai setup
openai.api_key = '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'

def parse_text_resume(text):
    data = {}
    data['name'] = re.findall(r'\b[A-Z][a-z]* [A-Z][a-z]*\b', text)
    data['email'] = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    data['phone'] = re.findall(r'\b\d{10}\b', text)
    
    # Extract professional experience: job titles, companies, duration
    experience = re.findall(r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* [0-9]{4} - (?:Present|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* [0-9]{4}))\s*([A-Za-z0-9 .,()/-]+?)\s*-\s*([A-Za-z0-9 .,()/-]+?)', text)
    data['experience'] = [{'title': exp[1], 'company': exp[2], 'duration': exp[0]} for exp in experience]
    
    # Extract education: degrees, institutions, graduation year
    education = re.findall(r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* [0-9]{4}) - (?:Present|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* [0-9]{4})\s*([A-Za-z0-9 .,()/-]+?)\s*-\s*([A-Za-z0-9 .,()/-]+?)', text)
    data['education'] = [{'degree': edu[1], 'institution': edu[2], 'graduation_year': edu[0]} for edu in education]
    
    # Extract skills: programming languages, frameworks, tools, databases
    skills = re.findall(r'\b(Java|Python|JavaScript|HTML|CSS|React|Angular|Node\.js|SQL|MongoDB|MySQL|PostgreSQL|Django|Flask|Spring|Bootstrap|Git|AWS|Azure|Linux|Windows)\b', text)
    data['skills'] = skills
    
    return data


def parse_pdf_resume(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return parse_text_resume(text)

def parse_docx_resume(docx_path):
    doc = docx.Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return parse_text_resume(text)

def parse_with_openai(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Extract the following information from this resume text:\n\n{text}",
        max_tokens=150
    )
    return response.choices[0].text.strip()