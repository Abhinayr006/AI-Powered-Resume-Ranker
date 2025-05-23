import re
import PyPDF2
import os

def get_pdf_text(file_path):
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            content = ""
            for page in reader.pages:
                content += page.extract_text()
            return content
    except Exception as error:
        print(f"Failed to read PDF {file_path}: {error}")
        return ""

def find_entities(text):
    email_pattern = r'\S+@\S+'
    emails = re.findall(email_pattern, text)
    # Updated regex to capture full names with capitalized words
    name_pattern = r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)+\b'
    names = re.findall(name_pattern, text)
    if names:
        names = [names[0]]
    return emails, names
