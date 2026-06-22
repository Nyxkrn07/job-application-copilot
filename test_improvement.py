from agents.resume_improvement import improve_resume

resume_text = """
Python Developer
FastAPI
Machine Learning
"""

job_description = """
Looking for Python Developer with FastAPI,
Docker and AWS experience.
"""

result = improve_resume(
    resume_text,
    job_description
)

print(result)