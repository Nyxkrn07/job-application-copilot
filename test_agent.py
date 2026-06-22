from agents.fit_analysis import analyze_resume_fit

# Sample resume
resume_text = """
Python Developer
FastAPI
SQL
Machine Learning
"""

# Sample Job Description
job_description = """
Looking for a Python Developer with FastAPI,
Docker and AWS experience.
"""

# Run analysis
result = analyze_resume_fit(
    resume_text,
    job_description
)

print(result)