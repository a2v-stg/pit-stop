import fitz  # PyMuPDF
import spacy
import re
import pyap
from transformers import pipeline
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")
#summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summarizer = pipeline("summarization")

JOB_KEYWORDS = {
    "Software Engineer": ["Python", "Django", "SQL", "Docker", "REST API"],
    "Data Scientist": ["Python", "Machine Learning", "TensorFlow", "SQL"],
    "Frontend Developer": ["JavaScript", "React", "CSS", "HTML"],
    "DevOps Engineer": ["Docker", "Kubernetes", "AWS", "CI/CD"]
}


def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text.strip()


def extract_info(text):
    """Extracts name, email, phone, address, and skills from profile text."""
    doc = nlp(text)
    
    # Extract Name
    name = next((ent.text for ent in doc.ents if ent.label_ == "PERSON"), None)

    # Extract Email & Phone
    email = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    phone = re.search(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)
    profile_url = re.search(r"https?://(?:www\.)?linkedin\.com/in/[a-zA-Z0-9-_%]+/?", text)

    # # Extract Address
    # addresses = pyap.parse(text, country="US")
    # address = addresses[0].full_address if addresses else None

    # Extract Skills
    all_skills = ["Python", "Java", "JavaScript", "React", "Django", "Machine Learning", "SQL", "Docker"]
    skills = ", ".join([skill for skill in all_skills if skill.lower() in text.lower()])

    # Summarize Profile
    if len(text.split()) > 100:
        try:
            # Summarize if the text is long enough
            summary_results = summarizer(text, max_length=150, min_length=50, do_sample=False)
            if summary_results and len(summary_results) > 0:
                summary = summary_results[0]["summary_text"]
            else:
                print(f"Not enough data to summarize")
                summary = text  # Fallback to original text if no summary is returned
        except Exception as e:
            summary = text  # Fallback to original text in case of an error
            print(f"Error during summarization: {e}")
    else:
        summary = text  # Use the original text if it's too short
        
    return {
        "name": name,
        "email": email.group(0) if email else None,
        "phone": phone.group(0) if phone else None,
        "skills": skills,
        "profile_url": profile_url,
        "summary": summary,
    }


def match_jobs(skills):
    """Matches profile skills to job roles."""
    skill_list = skills.lower().split(", ")
    matched_jobs = [job for job, req_skills in JOB_KEYWORDS.items() if any(skill in req_skills for skill in skill_list)]
    return ", ".join(matched_jobs) if matched_jobs else "No relevant jobs found"


def fitment_analysis(skills):
    """Determines the fitment analysis based on skills match."""
    skill_list = skills.lower().split(", ")
    # Define rules for good fit, maybe fit, and bad fit
    if "python" in skill_list and "django" in skill_list:
        return "Good Fit"
    elif "java" in skill_list and "javascript" in skill_list:
        return "Maybe"
    else:
        return "Bad Fit"

def process_profile(file_path):
    """Extracts profile information and analyzes fitment."""
    text = extract_text_from_pdf(file_path)
    extracted_data = extract_info(text)
    extracted_data["skills"] = extracted_data["skills"]
    extracted_data["fitment_analysis"] = fitment_analysis(extracted_data["skills"])
    return extracted_data
