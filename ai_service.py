import os

from dotenv import load_dotenv
from google import genai


# Load variables from .env
load_dotenv()


# Get API key
API_KEY = os.getenv("GEMINI_API_KEY")


if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Please add your Gemini API key to the .env file."
    )


# Create Gemini client
client = genai.Client(api_key=API_KEY)


# --------------------------------------------------
# Common AI function
# --------------------------------------------------

def ask_gemini(prompt):

    try:

        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            input=prompt
        )

        return interaction.output_text

    except Exception as e:

        print("Gemini API Error:")
        print(e)

        raise e


# --------------------------------------------------
# AI PROFESSIONAL SUMMARY
# --------------------------------------------------

def generate_summary(user_details):

    prompt = f"""
You are a professional resume-writing assistant.

Create a professional resume summary using the
candidate information below.

Candidate information:
{user_details}

Requirements:
- Write 3 to 4 sentences.
- Make it suitable for a fresher or entry-level candidate.
- Use professional language.
- Highlight relevant skills, education and projects.
- Do not invent experience.
- Do not invent achievements.
- Do not invent numbers.
- Keep the summary concise.
"""

    return ask_gemini(prompt)


# --------------------------------------------------
# AI BULLET POINT IMPROVER
# --------------------------------------------------

def improve_bullet_point(bullet):

    prompt = f"""
You are a professional resume-writing assistant.

Improve the following resume bullet point.

Original bullet:
{bullet}

Requirements:
- Start with a strong action verb.
- Make the sentence professional.
- Keep the original meaning.
- Make it concise.
- Do not invent achievements.
- Do not invent statistics.
- Do not invent technologies that were not mentioned.

Return only the improved bullet point.
"""

    return ask_gemini(prompt)


# --------------------------------------------------
# JOB DESCRIPTION MATCHER
# --------------------------------------------------

def analyze_job_match(resume, job_description):

    prompt = f"""
You are a resume and job-description analysis assistant.

Analyze the candidate's resume against the job description.

RESUME:
{resume}


JOB DESCRIPTION:
{job_description}


Provide the following:

1. Matching Skills

List the skills from the resume that match
the job description.


2. Missing Keywords

Identify important skills or keywords mentioned
in the job description that are not clearly present
in the resume.


3. Resume Improvement Suggestions

Give practical suggestions for improving the resume.


4. Relevant Technologies

List technologies from the resume that are
relevant to the job.


5. Overall Analysis

Give a short explanation of how well the resume
matches the job description.

Important:
- Do not invent qualifications.
- Do not claim the candidate has a skill unless
  it appears in the resume.
"""

    return ask_gemini(prompt)


# --------------------------------------------------
# AI COVER LETTER
# --------------------------------------------------

def generate_cover_letter(resume, job_description):

    prompt = f"""
You are a professional career-writing assistant.

Create a professional cover letter based on the
candidate resume and job description.

RESUME:
{resume}


JOB DESCRIPTION:
{job_description}


Requirements:
- Suitable for an entry-level candidate.
- Professional but natural tone.
- Mention relevant skills and projects.
- Connect the candidate's background to the role.
- Do not invent experience.
- Do not invent achievements.
- Do not invent numbers.
- Keep the cover letter concise.
"""

    return ask_gemini(prompt)