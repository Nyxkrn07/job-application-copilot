# Job Application Co-Pilot

## Project Overview

Job Application Co-Pilot is a multi-agent AI application that helps job seekers improve their job applications. The system analyzes a resume and job description, then generates a complete application kit including resume analysis, resume improvements, ATS-optimized resume content, cover letter generation, and interview preparation questions.

## Objective

The goal of this project is to simplify the job application process by using AI agents to provide personalized recommendations and application materials based on a candidate's resume and a target job description.

## Features

* Upload Resume PDF
* Extract Resume Text
* Resume and Job Description Fit Analysis
* Resume Improvement Suggestions
* ATS-Friendly Resume Rewriting
* Cover Letter Generation
* Interview Questions and Answers Generation
* Save Generated Results to SQLite Database
* View Saved Applications

## Technology Stack

### Backend

* Python
* FastAPI
* Pydantic
* SQLite

### AI Integration

* Groq API
* Llama 3.3 70B Versatile Model

### Frontend

* HTML
* CSS
* JavaScript

### Libraries

* pypdf
* python-dotenv
* uvicorn

## Project Structure

JobApplicationCopilot/

├── agents/

│ ├── fit_analysis.py

│ ├── resume_improvement.py

│ ├── resume_rewriter.py

│ ├── cover_letter.py

│ └── interview_qa.py

├── frontend/

│ ├── index.html

│ ├── style.css

│ └── script.js

├── database.py

├── main.py

├── job_applications.db

├── .env

└── requirements.txt

## API Endpoints

### Upload Resume

POST /upload-resume

### Resume Fit Analysis

POST /fit-analysis

### Resume Improvement

POST /resume-improvement

### Resume Rewriter

POST /rewrite-resume

### Cover Letter Generator

POST /cover-letter

### Interview Questions Generator

POST /interview-qa

### Generate Complete Application Kit

POST /generate-application-kit

### View Saved Applications

GET /applications

## Database

The project uses SQLite to store generated application kits.

Stored information includes:

* Resume Text
* Job Description
* Fit Analysis
* Resume Improvements
* Rewritten Resume
* Cover Letter
* Interview Questions

## How to Run

1. Clone or download the project.
2. Create a virtual environment.
3. Install dependencies.

pip install -r requirements.txt

4. Add your Groq API key to the .env file.

GROQ_API_KEY=your_api_key_here

5. Start the FastAPI server.

uvicorn main:app --reload

6. Open Swagger UI.

http://127.0.0.1:8000/docs

7. Open the frontend.

frontend/index.html

## Future Improvements

* User Authentication
* Multiple Resume Support
* PDF Export Feature
* Job Recommendation Engine
* Cloud Database Integration
* Dashboard Analytics

## Author

Karan Kumar Rana

Capstone Project – New Age Software Developer Program
