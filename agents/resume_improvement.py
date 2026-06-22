from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def improve_resume(resume_text, job_description):

    query = f"""
You are an expert resume reviewer.

Resume:
{resume_text}

Job Description:
{job_description}

Analyze resume and suggest improvements:

1. Missing skills
2. Resume improvement suggestions
3. Sections that should be strengthened
4. Keywords that should be added
5. Overall recommendations

Provide the response in this format:

MISSING SKILLS:
- Skill 1
- Skill 2

RESUME IMPROVEMENTS:
- Improvement 1
- Improvement 2

KEYWORDS TO ADD:
- Keyword 1
- Keyword 2

FINAL RECOMMENDATION:
Short summary
"""
# Call LLM with resume and job description
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ]
    )
    return response.choices[0].message.content