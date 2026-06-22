from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()   

groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)   

def generate_cover_letter(resume_text, job_description):

    query = f"""    
You are an expert cover letter writer and career coach.

resume:
{resume_text}

Job Description:
{job_description}

Write a short professional cover letter (maximum 150 words) that highlights only the most relevant skills and experience from the resume.
Rules:
1. Do NOT invent any skills or experience.
2. Use only information from the resume.
3. Focus on skills that match the job description.
4. Keep the letter concise.
5. Include a short introduction, body, and conclusion.

Return only the cover letter text. Keep it under 150 words.
    """

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