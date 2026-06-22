from agents.interview_qa import generate_interview_qa, generate_interview_questions

resume_text = """
Python Developer
FastAPI
Machine Learning
"""

job_description = """
Looking for a Python Developer with FastAPI,
Docker and AWS experience.
"""

result = generate_interview_qa(
    resume_text,
    job_description
)

print(result)
