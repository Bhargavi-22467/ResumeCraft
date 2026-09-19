from ai_service import (
    generate_summary,
    improve_bullet_point,
    analyze_job_match,
    generate_cover_letter
)

from flask import Flask, render_template, request, redirect, url_for, send_file
from database import init_db, save_resume, get_resume
from pdf_generator import generate_pdf
import os

app = Flask(__name__)

init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/builder")
def builder():
    return render_template("builder.html")


@app.route("/create", methods=["POST"])
def create_resume():

    resume_data = {
        "name": request.form.get("name", ""),
        "email": request.form.get("email", ""),
        "phone": request.form.get("phone", ""),
        "location": request.form.get("location", ""),
        "linkedin": request.form.get("linkedin", ""),
        "github": request.form.get("github", ""),
        "summary": request.form.get("summary", ""),
        "education": request.form.get("education", ""),
        "skills": request.form.get("skills", ""),
        "experience": request.form.get("experience", ""),
        "projects": request.form.get("projects", ""),
        "certifications": request.form.get("certifications", ""),
        "achievements": request.form.get("achievements", ""),
        "template": request.form.get("template", "modern")
    }

    resume_id = save_resume(resume_data)

    return redirect(url_for("preview", resume_id=resume_id))


@app.route("/preview/<int:resume_id>")
def preview(resume_id):

    resume = get_resume(resume_id)

    if not resume:
        return "Resume not found", 404

    return render_template(
        "preview.html",
        resume=resume
    )


@app.route("/download/<int:resume_id>")
def download_pdf(resume_id):

    resume = get_resume(resume_id)

    if not resume:
        return "Resume not found", 404

    filename = f"resume_{resume_id}.pdf"

    pdf_path = generate_pdf(resume, filename)

    return send_file(
        pdf_path,
        as_attachment=True,
        download_name=filename
    )
@app.route("/ai-summary", methods=["POST"])
def ai_summary():

    details = request.form.get("details", "")

    if not details:
        return "Please provide applicant details.", 400

    try:

        result = generate_summary(details)

        return result

    except Exception as e:

        return f"AI error: {str(e)}", 500

@app.route("/ai-bullet", methods=["POST"])
def ai_bullet():

    bullet = request.form.get("bullet", "")

    if not bullet:
        return "Please provide a bullet point.", 400

    try:

        result = improve_bullet_point(bullet)

        return result

    except Exception as e:

        return f"AI error: {str(e)}", 500

@app.route("/ai-job-match", methods=["POST"])
def ai_job_match():

    resume = request.form.get("resume", "")

    job_description = request.form.get(
        "job_description",
        ""
    )

    if not resume or not job_description:

        return (
            "Resume and job description are required.",
            400
        )

    try:

        result = analyze_job_match(
            resume,
            job_description
        )

        return result

    except Exception as e:

        return f"AI error: {str(e)}", 500


@app.route("/ai-tools")
def ai_tools():

    return render_template("ai_tools.html")

if __name__ == "__main__":
    app.run(debug=True)