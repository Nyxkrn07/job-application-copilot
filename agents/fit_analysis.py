from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Create Groq client
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume_fit(resume_text, job_description):

    query = f"""
Analyze the following resume and job description for fit:

Resume:
{resume_text}

Job Description:
{job_description}

# Function to  analyze resume against job description
Provide the response in this format:

FIT SCORE: Give only a numeric score between 0 and 100

MATCHING SKILLS:
- Skill 1
- Skill 2

MISSING SKILLS:
- Skill 1
- Skill 2

RESUME IMPROVEMENT SUGGESTIONS:
- Suggestion 1
- Suggestion 2

FINAL VERDICT:
Short summary of candidate suitability.
"""

    # Send prompt to Groq AI
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ]
    )

    # Return AI-generated analysis
    return response.choices[0].message.content