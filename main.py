from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from database import save_application, get_all_applications
from agents.interview_qa import generate_interview_qa
from agents.cover_letter import generate_cover_letter
from agents.fit_analysis import analyze_resume_fit
from agents.resume_improvement import improve_resume
from agents.resume_rewriter import rewrite_resume
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, File
from pypdf import PdfReader
import tempfile
import os

# Create FastAPI application instance and Home endpoint to verify API is running
app = FastAPI()

# Allow frontend to communicate with FastAPI

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/")
# def home():
#     """
#     Home endpoint to verify that the API is running.

#     Returns:
#         dict: A simple status message.
#     """
#     return {"message": "Job Application Copilot Running"}


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    """
    Upload and parse a PDF resume.

    Workflow:
    1. Receive PDF file from the user.
    2. Save it temporarily on the server.
    3. Extract text from all pages using PyPDF.
    4. Delete the temporary file.
    5. Return the extracted text.

    Args:
        file (UploadFile): PDF resume uploaded by the user.

    Returns:
        dict: Filename and extracted resume text.
    """
    # Create a temporary file to store the uploaded PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(await file.read())
        temp_path = temp_file.name

    try:
        # Open the PDF file
        reader = PdfReader(temp_path)

        # Store extracted text from all pages
        resume_text = ""

        # Loop through every page in the PDF
        for page in reader.pages:
            page_text = page.extract_text()

            # Check if text exists before appending
            if page_text:
                resume_text += page_text + "\n"

        # Return extracted data
        return {
            "filename": file.filename,
            "resume_text": resume_text
        }

    finally:
        # Remove temporary file to avoid storage buildup
        if os.path.exists(temp_path):
            os.remove(temp_path)

from pydantic import BaseModel

#model to receive job description from frotend
class JobDescription(BaseModel):
    jd_text: str

class FitAnalysisRequest(BaseModel):
    resume_text: str
    job_description: str


@app.post("/resume-improvement")
def resume_improvement(data: FitAnalysisRequest):
    """
    Endpoint to improve a resume based on a job description.

    Args:
        data (FitAnalysisRequest): Contains the resume text and job description.

    Returns:
        dict: AI-generated suggestions for improving the resume.
    """
    result = improve_resume(data.resume_text, data.job_description)
    return {"improved_resume": result}

def improve_resume_endpoint(resume_text: str, job_description: str):
    """
    Endpoint to improve a resume based on a job description.
    """
    result = improve_resume(resume_text, job_description)
    return {"improved_resume": result}


@app.post("/job-description")
def receive_job_description(jd: JobDescription):
    """
    Endpoint to receive job description text from the frontend.

    Args:
        jd (JobDescription): Contains the job description entered by the user.

    Returns:
        dict: Confirmation message and received job description.
    """

    return {
        "message": "Job description received successfully",
        "job_description": jd.jd_text
    }


@app.post("/fit-analysis")
def fit_analysis(data: FitAnalysisRequest):
    """
    Compare resume and job description using AI.
    """

    result = analyze_resume_fit(
        data.resume_text,
        data.job_description
    )

    return {
        "fit_analysis": result
    }

# Generate ATS optimized resume
@app.post("/rewrite-resume")
def rewrite_resume_endpoint(data: FitAnalysisRequest):
    """
    Endpoint to rewrite a resume based on a job description.
    """
    result = rewrite_resume(data.resume_text, data.job_description)
    return {"rewritten_resume": result}


@app.post("/cover-letter")
def cover_letter(data: FitAnalysisRequest):

    result = generate_cover_letter(
        data.resume_text,
        data.job_description
    )

    return {
        "cover_letter": result
    }

@app.post("/interview-qa")
def interview_qa(data: FitAnalysisRequest):
    """
    Generate interview questions and answers.
    """

    result = generate_interview_qa(
        data.resume_text,
        data.job_description
    )

    return {
        "interview_qa": result
    }

# Main orchestration endpoint
# Runs all AI agents and generates a complete application kit
# from a resume and job description

@app.post("/generate-application-kit")
def generate_application_kit(data: FitAnalysisRequest):

    # Trim inputs once — all agents use short version
    resume_short = data.resume_text[:1500]
    jd_short = data.job_description[:500]

    fit_result          = analyze_resume_fit(resume_short, jd_short)
    improvement_result  = improve_resume(resume_short, jd_short)
    rewritten_resume    = rewrite_resume(resume_short, jd_short)
    cover_letter        = generate_cover_letter(resume_short, jd_short)
    interview_questions = generate_interview_qa(resume_short, jd_short)

    try:
        save_application(
            data.resume_text,  # save full version in DB
            data.job_description,
            fit_result,
            improvement_result,
            rewritten_resume,
            cover_letter,
            interview_questions
        )
        print("DATABASE SAVE SUCCESS")
    except Exception as e:
        print("DATABASE ERROR", e)

    return {
        "fit_analysis": fit_result,
        "resume_improvement": improvement_result,
        "rewritten_resume": rewritten_resume,
        "cover_letter": cover_letter,
        "interview_qa": interview_questions
    }

@app.get("/applications")
def view_applications():
    """
   # Retrieve all saved applications from database
    """

    applications = get_all_applications()

    return{
        "applications": applications
    }

# Bottom of main.py — last two lines
frontend_path = os.path.join(os.path.dirname(__file__), "frontend")
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")