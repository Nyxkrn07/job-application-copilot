from agents.resume_rewriter import rewrite_resume

resume_text = """
Python Developer
FastAPI
Machine Learning
"""

job_description = """
Looking for Python Developer with FastAPI,
Docker and AWS experience.
"""

result = rewrite_resume(
    resume_text,
    job_description
)   

print(result)