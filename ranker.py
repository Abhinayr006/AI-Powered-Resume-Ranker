import spacy
import csv
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from helpers import get_pdf_text, find_entities

nlp = spacy.load("en_core_web_sm")

def evaluate_resumes(job_desc, resume_files):
    vectorizer = TfidfVectorizer()
    job_vector = vectorizer.fit_transform([job_desc])

    scored_list = []
    for file_path in resume_files:
        content = get_pdf_text(file_path)
        emails, names = find_entities(content)
        resume_vector = vectorizer.transform([content])
        similarity_score = cosine_similarity(job_vector, resume_vector)[0][0]
        scored_list.append((names, emails, similarity_score))

    scored_list.sort(key=lambda x: x[2], reverse=True)
    return scored_list

def export_to_csv(scored_resumes, output_file="ranked_resumes.csv"):
    try:
        with open(output_file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Rank", "Name", "Email", "Similarity"])
            for idx, (names, emails, score) in enumerate(scored_resumes, start=1):
                name = names[0] if names else "N/A"
                email = emails[0] if emails else "N/A"
                writer.writerow([idx, name, email, score])
    except Exception as err:
        print(f"Failed to write CSV {output_file}: {err}")

def main():
    job_description = "NLP Specialist: Develop and implement NLP algorithms. Proficiency in Python, NLP libraries, and ML frameworks required."
    resumes = ["resume1.pdf", "resume2.pdf", "resume3.pdf"]

    results = evaluate_resumes(job_description, resumes)

    for rank, (names, emails, score) in enumerate(results, start=1):
        print(f"Rank {rank}: Names: {names}, Emails: {emails}, Similarity: {score:.2f}")

    export_to_csv(results)

if __name__ == "__main__":
    main()
