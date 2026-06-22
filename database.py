import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("job_applications.db")

# Create cursor to execute SQL commands
cursor = conn.cursor()

# Create applications table if it does not already exist
# Create applications table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resume_text TEXT,
    job_description TEXT,
    fit_analysis TEXT,
    resume_improvement TEXT,
    rewritten_resume TEXT,
    cover_letter TEXT,
    interview_qa TEXT
)
""")

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database created successfully!")

import sqlite3

# Save application kit into SQLite database
def save_application(
    resume_text,
    job_description,
    fit_analysis,
    resume_improvement,
    rewritten_resume,
    cover_letter,
    interview_qa
):

    conn = sqlite3.connect("job_applications.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO applications (
        resume_text,
        job_description,
        fit_analysis,
        resume_improvement,
        rewritten_resume,
        cover_letter,
        interview_qa
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        resume_text,
        job_description,
        fit_analysis,
        resume_improvement,
        rewritten_resume,
        cover_letter,
        interview_qa
    ))

    conn.commit()
    conn.close()

    # Fetch all saved applications from database
def get_all_applications():

    conn = sqlite3.connect("job_applications.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM applications")

    applications = cursor.fetchall()

    conn.close()

    return applications