from flask import Flask, render_template, request, send_file, session
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv
import os
from helpers import get_pdf_text, find_entities

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

nlp = spacy.load("en_core_web_sm")

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        job_desc = request.form.get('job_description')
        resumes = request.files.getlist('resume_files')

        upload_dir = "uploads"
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        processed = []
        for resume in resumes:
            path = os.path.join(upload_dir, resume.filename)
            resume.save(path)

            text = get_pdf_text(path)
            emails, names = find_entities(text)
            processed.append((names, emails, text))

        vectorizer = TfidfVectorizer()
        job_vec = vectorizer.fit_transform([job_desc])

        scored = []
        for names, emails, text in processed:
            resume_vec = vectorizer.transform([text])
            score = cosine_similarity(job_vec, resume_vec)[0][0] * 100
            scored.append((names, emails, score))

        scored.sort(key=lambda x: x[2], reverse=True)
        results = scored
        # Store results in session for CSV download
        session['results'] = [(names, emails, score) for names, emails, score in results]

    return render_template('home.html', results=results)

@app.route('/download_csv')
def download_csv():
    filename = "ranked_resumes.csv"
    try:
        results = session.get('results', [])
        with open(filename, "w", newline='') as f:
            f.write("Rank,Name,Email,Similarity\n")
            for rank, (names, emails, similarity) in enumerate(results, start=1):
                name = names[0] if names else "N/A"
                email = emails[0] if emails else "N/A"
                f.write(f"{rank},{name},{email},{similarity}\n")
    except Exception as e:
        print(f"CSV write error: {e}")

    full_path = os.path.abspath(filename)
    return send_file(full_path, as_attachment=True, download_name=filename)

if __name__ == '__main__':
    app.run(debug=True)
