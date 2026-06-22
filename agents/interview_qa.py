from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# Create Groq client
groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
    )

def generate_interview_qa(resume_text, job_description):

    query = f"""
You are an expert technical interviewer.

Resume:
{resume_text}

Job Description:
{job_description}

Based on the resume and job description below, generate 5 interview questions and answers.

Rules:
1. Mix conceptual, behavioral, and technical questions.
2. Write answers in first person ("I").
3. Keep each answer between 2-4 sentences.
4. Use resume details when relevant.
5. Do not include interviewer notes.
6. Keep answers concise and interview-ready.
Format strictly as:

---
Question 1 [Type: Conceptual]:
<question>

Answer:
<candidate answer>

---
Question 2 [Type: Behavioral]:
<question>

Answer:
<candidate answer>
---
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