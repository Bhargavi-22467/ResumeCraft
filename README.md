# **ResumeCraft – AI-Powered Online Resume Builder**

ResumeCraft is a web-based resume builder that allows users to create professional resumes, preview them, and download them as PDF files. The AI-powered Version 2 also helps users improve resume content, generate professional summaries, analyze job descriptions, identify missing keywords, and generate customized cover letters.

---

## 🚀 Features

### Version 1 – Resume Builder

* 📝 Create a professional resume
* 👤 Add personal information
* 🎓 Add education details
* 💻 Add technical and soft skills
* 💼 Add internship/experience details
* 🚀 Add projects
* 📜 Add certifications
* 🏆 Add achievements
* 🎨 Select resume templates
* 👀 Preview resume before downloading
* 📄 Generate PDF resume
* ⬇️ Download resume
* 💾 Store resume information using SQLite
* 📱 Responsive user interface

### Version 2 – AI Resume Features

* 🤖 AI-generated professional summary
* ✍️ AI-powered resume bullet-point improvement
* 🎯 Job description matching
* 🔍 Missing keyword identification
* 📊 Resume improvement suggestions
* 📝 AI-generated cover-letter draft
* 💼 Job-specific resume customization

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Database

* SQLite

### PDF Generation

* ReportLab

### AI

* Google Gemini API
* Google Gen AI Python SDK

### Environment Management

* Python Virtual Environment
* python-dotenv

---

## 📂 Project Structure

```text
ResumeCraft/
│
├── venv/
│
├── app.py
├── database.py
├── pdf_generator.py
├── ai_service.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── database/
│   └── resumes.db
│
├── generated_resumes/
│
├── templates/
│   ├── index.html
│   ├── builder.html
│   ├── preview.html
│   └── ai_tools.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        └── script.js
```

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

Open PowerShell or Command Prompt and run:

```bash
git clone https://github.com/your-username/ResumeCraft.git
```

Move into the project folder:

```bash
cd ResumeCraft
```

---

## 2. Create a Virtual Environment

Run:

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\activate
```

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

After activation, you should see:

```text
(venv)
```

before your terminal path.

---

## 4. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

If you are setting up Version 2 manually, you can also install:

```bash
pip install flask reportlab google-genai python-dotenv
```

---

# 🔑 AI API Configuration

Version 2 requires a Google Gemini API key.

Create a file named:

```text
.env
```

in the project root.

Add:

```text
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Replace:

```text
YOUR_API_KEY_HERE
```

with your actual API key.

### ⚠️ Important

Never upload your `.env` file to GitHub.

The `.gitignore` file should contain:

```text
.env
venv/
__pycache__/
*.pyc
database/resumes.db
generated_resumes/
```

---

# ▶️ How to Run the Project

Make sure your virtual environment is activated.

Run:

```bash
python app.py
```

You should see something similar to:

```text
* Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🖥️ Application Pages

## 🏠 Home Page

The home page provides access to:

* Resume Builder
* AI Resume Tools
* Project information

---

## 📝 Resume Builder

Users can enter:

* Full name
* Email
* Phone number
* Location
* LinkedIn
* GitHub
* Professional summary
* Education
* Skills
* Experience
* Projects
* Certifications
* Achievements

Users can also select a resume template.

---

## 👀 Resume Preview

After submitting the form, the application generates a formatted resume preview.

The user can:

* Review the resume
* Create another resume
* Download the resume as PDF

---

## 📄 PDF Generation

ResumeCraft uses **ReportLab** to generate downloadable PDF resumes.

Generated files are stored in:

```text
generated_resumes/
```

Example:

```text
generated_resumes/resume_1.pdf
```

---

# 🤖 AI Features

## 1. AI Professional Summary

The user provides information about their education, skills, projects, and career interests.

The AI generates a professional resume summary.

### Example input

```text
B.Tech Computer Science student with knowledge of
Python, machine learning and Flask. Developed
academic AI and machine learning projects.
Interested in AI engineering.
```

### Output

The AI produces a polished professional summary based on the supplied information.

---

## 2. AI Bullet Point Improver

Users can enter simple project or experience descriptions.

The AI rewrites them into concise, professional resume bullet points.

### Example

Input:

```text
Created a machine learning project for predicting bike rentals.
```

The AI can produce a stronger resume-oriented version while preserving the original meaning.

---

## 3. Job Description Matcher

Users provide:

```text
Resume
+
Job Description
```

The AI analyzes both and identifies:

* Matching skills
* Relevant technologies
* Missing keywords
* Potential improvement areas

---

## 4. AI Cover Letter Generator

The user provides:

```text
Resume
+
Job Description
```

The application generates a professional cover-letter draft tailored to the provided information.

The generated content should be reviewed by the user before submission.

---

# 🔄 Application Workflow

## Version 1

```text
User
  ↓
Home Page
  ↓
Resume Builder
  ↓
Enter Resume Information
  ↓
Select Template
  ↓
Flask Backend
  ↓
SQLite Database
  ↓
Resume Preview
  ↓
ReportLab
  ↓
PDF Resume
  ↓
Download
```

## Version 2

```text
User
  ↓
Resume / Job Description
  ↓
Flask Backend
  ↓
AI Service
  ↓
Gemini API
  ↓
AI Analysis
  ↓
Summary / Bullet Improvement /
Job Matching / Cover Letter
  ↓
User
```

---

# 🗄️ Database

ResumeCraft uses SQLite to store resume information.

The database is automatically created when the application starts.

Database location:

```text
database/resumes.db
```

The resume table contains fields such as:

```text
id
name
email
phone
location
linkedin
github
summary
education
skills
experience
projects
certifications
achievements
template
```

---

# 🧪 Testing

After starting the application, test the following:

### Resume Builder

* [ ] Home page loads
* [ ] Resume form opens
* [ ] Required fields work
* [ ] Resume can be submitted
* [ ] Resume preview appears
* [ ] PDF can be downloaded
* [ ] PDF contains entered information

### AI Features

* [ ] AI Tools page opens
* [ ] Professional summary generation works
* [ ] Bullet improvement works
* [ ] Job description analysis works
* [ ] Cover-letter generation works
* [ ] Invalid/empty input is handled
* [ ] API key is loaded from `.env`

---

# 🛡️ Security Considerations

* API keys are stored in `.env`
* `.env` should not be committed to GitHub
* Generated files are excluded from Git
* SQLite database files are excluded from Git
* User input should be validated before processing
* AI-generated content should be reviewed before being used in applications

---

# 🔮 Future Enhancements

Possible future improvements include:

* 👤 User registration and login
* 🔐 Authentication
* ☁️ Cloud database
* 📚 Multiple saved resumes
* 🎨 More professional templates
* 🎨 Custom color themes
* 🖋️ Font customization
* 🔄 Drag-and-drop resume sections
* 📊 More detailed resume analysis
* 🎯 Job-specific resume generation
* 📈 Resume analytics
* 📤 Shareable resume links
* 📱 Improved mobile UI
* 🌐 Deployment to a cloud platform
* 📥 Import resume from an existing PDF
* 🔗 LinkedIn profile import
* 📄 DOCX export
* 🧠 More advanced AI resume optimization

---

# 🎯 Use Cases

ResumeCraft can be useful for:

* College students
* Fresh graduates
* Job seekers
* Internship applicants
* Career switchers
* Professionals creating multiple job-specific resumes
