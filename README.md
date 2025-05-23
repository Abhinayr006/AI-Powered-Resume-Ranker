# AI-Powered-Resume-Ranker

## Overview
Resume Analyzer is a Flask web application that ranks uploaded resumes based on their similarity to a given job description. It uses natural language processing (NLP) techniques with SpaCy and machine learning methods with scikit-learn to analyze and score resumes. The results can be viewed on the web interface and downloaded as a CSV file.

## Features
- Upload multiple PDF resumes
- Input a job description
- Analyze and rank resumes based on similarity to the job description
- View ranked results on the webpage
- Download ranked results as a CSV file
- Simple and clean user interface with dark mode toggle

## Requirements
- Python 3.7 or higher
- Flask
- SpaCy
- scikit-learn
- PyPDF2

## Installation

1. Clone the repository:
   ```bash
   git clone <https://github.com/Abhinayr006/AI-Powered-Resume-Ranker>
   cd resume-ranker-main
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required Python packages:
   ```bash
   pip install flask spacy scikit-learn PyPDF2
   ```

4. Download the SpaCy English model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Running the Application

Run the Flask app using:

```bash
python main_app.py
```

By default, the app will run in debug mode on `http://127.0.0.1:5000/`.

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Enter the job description in the provided text area.
   For example:
   ```bash
   Computer Vision, Image Processing, Reinforcement Learning, TensorFlow, Data Visualization, Statistical Analysis
   ```
3. Upload one or more PDF resumes using the file upload input.
4. Click the "Analyze Resumes" button.
5. The ranked resumes will be displayed in a table showing rank, name, email, and similarity percentage.
6. You can download the ranked results as a CSV file by clicking the "Download CSV" link.

## File Structure

- `main_app.py`: Main Flask application file containing routes and logic.
- `helpers.py`: Helper functions for extracting text and entities from PDF resumes.
- `ranker.py`: (If applicable) Additional ranking logic (not directly referenced in main_app.py).
- `ranked_resumes.csv`: CSV file generated with ranked resume results.
- `templates/`: Contains HTML templates (e.g., `home.html`).
- `static/`: Contains static files such as CSS (`styles_main.css`).
- `uploads/`: Directory where uploaded resumes are saved temporarily.

## Notes

- The app uses Flask sessions to store ranking results temporarily for CSV download.
- The secret key in `main_app.py` should be changed to a secure random value for production use.
- Uploaded resumes are saved in the `uploads/` folder; ensure this folder has appropriate permissions.
- The app currently supports PDF resumes only.
- The dark mode toggle is available in the UI, but ensure the corresponding CSS files are present or adjust as needed.

---

Feel free to contribute or raise issues on the GitHub repository.
