from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)       
def rewrite_resume(resume_text, job_description):

    query = f"""
    You are an expert resume rewriter.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Task:

    Analyze the resume and rewrite it to better match the job description. 
    Focus on:

    Requirements:

1. Keep all information truthful.
2. Do NOT add skills, tools, certifications, projects, or experience that are not present in the original resume.
3. If a required skill is missing, mention it in a "Recommended Skills" section instead of pretending the candidate has it.
4. Improve wording and formatting.
5. Create sections:
   - Professional Summary
   - Technical Skills
   - Experience / Projects
6. Optimize for ATS screening.
7. Use keywords from the job description only when they already exist in the resume.

8. IMPORTANT RULES:

1. Never invent experience, projects, certifications, or skills.
2. Only use information already present in the resume.
3. If the job description contains skills that are missing from the resume, place them under a separate section called "Recommended Skills".
4. Do not add missing skills to the candidate's actual resume content.
5. Explain briefly why the skills are recommended.

Format:

### Recommended Skills

- Skill 1
- Skill 2

Why:
These skills appear in the job description but are not present in the current resume.


    Return the rewritten resume in clean professional and ATS-friendly rewritten resume.
    """

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": query}
        ]
    )

    return response.choices[0].message.content