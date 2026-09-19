import sqlite3
import os


DATABASE_FOLDER = "database"
DATABASE_PATH = os.path.join(DATABASE_FOLDER, "resumes.db")


def get_connection():
    os.makedirs(DATABASE_FOLDER, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    connection.row_factory = sqlite3.Row

    return connection


def init_db():

    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            location TEXT,
            linkedin TEXT,
            github TEXT,
            summary TEXT,
            education TEXT,
            skills TEXT,
            experience TEXT,
            projects TEXT,
            certifications TEXT,
            achievements TEXT,
            template TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_resume(data):

    connection = get_connection()

    cursor = connection.execute("""
        INSERT INTO resumes (
            name,
            email,
            phone,
            location,
            linkedin,
            github,
            summary,
            education,
            skills,
            experience,
            projects,
            certifications,
            achievements,
            template
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["name"],
        data["email"],
        data["phone"],
        data["location"],
        data["linkedin"],
        data["github"],
        data["summary"],
        data["education"],
        data["skills"],
        data["experience"],
        data["projects"],
        data["certifications"],
        data["achievements"],
        data["template"]
    ))

    connection.commit()

    resume_id = cursor.lastrowid

    connection.close()

    return resume_id


def get_resume(resume_id):

    connection = get_connection()

    resume = connection.execute(
        "SELECT * FROM resumes WHERE id = ?",
        (resume_id,)
    ).fetchone()

    connection.close()

    return resume