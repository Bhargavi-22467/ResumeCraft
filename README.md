# ResumeCraft – AI-Powered Online Resume Builder

ResumeCraft is a web-based resume builder that helps users create professional resumes, preview them, and download them as PDF files. Version 2 adds AI features for improving resume content and tailoring it to job descriptions.

---

## 🚀 Features

### Version 1

* 📝 Create professional resumes
* 👤 Add personal, education, skills, experience, projects and certifications
* 🎨 Select resume templates
* 👀 Preview resumes
* 📄 Generate and download PDF resumes
* 💾 Store resume data using SQLite
* 📱 Responsive interface

### Version 2 – AI Features

* 🤖 Generate professional summaries
* ✍️ Improve resume bullet points
* 🎯 Match resumes with job descriptions
* 🔍 Identify missing keywords
* 📊 Get resume improvement suggestions
* 📝 Generate customized cover letters

---

## 🛠️ Technologies

**Frontend**

* HTML5
* CSS3
* JavaScript

**Backend**

* Python
* Flask

**Database**

* SQLite

**PDF**

* ReportLab

**AI**

* Google Gemini API
* Google Gen AI SDK

**Other**

* Python Virtual Environment
* python-dotenv

---

## 📂 Project Structure

```text
ResumeCraft/
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
    └── js/
        └── script.js
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ResumeCraft.git
cd ResumeCraft
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate it

**PowerShell:**

```powershell
.\venv\Scripts\activate
```

**Command Prompt:**

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 AI Configuration

Create a `.env` file in the project folder:

```text
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Never upload the `.env` file to GitHub.

Your `.gitignore` should include:

```text
.env
venv/
__pycache__/
*.pyc
database/resumes.db
generated_resumes/
```

---

## ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🔄 Application Workflow

### Version 1

```text
User
 ↓
Resume Builder
 ↓
Enter Information
 ↓
Select Template
 ↓
Resume Preview
 ↓
Generate PDF
 ↓
Download
```

### Version 2

```text
Resume + Job Description
 ↓
AI Service
 ↓
Gemini API
 ↓
Summary / Bullet Improvement /
Keyword Analysis / Cover Letter
```

---

## 🗄️ Database

Resume data is stored in:

```text
database/resumes.db
```

The database is automatically created when the application starts.

---

## 🔮 Future Enhancements

* User authentication
* Multiple saved resumes
* More resume templates
* DOCX export
* Resume sharing through links
* Cloud deployment
* Advanced ATS analysis
* Job-specific resume generation
* LinkedIn/PDF resume import

---

## 🎯 Use Cases

ResumeCraft is useful for:

* College students
* Fresh graduates
* Internship applicants
* Job seekers
* Career switchers
* Professionals

---

## 📌 Project Title

**ResumeCraft – AI-Powered Online Resume Builder**
