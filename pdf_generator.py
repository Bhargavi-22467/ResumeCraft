from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable
)
import os


def generate_pdf(resume, filename):

    output_folder = "generated_resumes"

    os.makedirs(output_folder, exist_ok=True)

    file_path = os.path.join(output_folder, filename)

    document = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=45,
        leftMargin=45,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    name_style = ParagraphStyle(
        "NameStyle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=22,
        spaceAfter=8
    )

    contact_style = ParagraphStyle(
        "ContactStyle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=9,
        spaceAfter=15
    )

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontSize=12,
        spaceBefore=10,
        spaceAfter=5
    )

    normal_style = ParagraphStyle(
        "NormalStyle",
        parent=styles["Normal"],
        fontSize=9.5,
        leading=14,
        spaceAfter=5
    )

    story = []

    story.append(
        Paragraph(resume["name"], name_style)
    )

    contact = " | ".join(
        value for value in [
            resume["email"],
            resume["phone"],
            resume["location"]
        ]
        if value
    )

    story.append(
        Paragraph(contact, contact_style)
    )

    if resume["linkedin"] or resume["github"]:

        links = " | ".join(
            value for value in [
                resume["linkedin"],
                resume["github"]
            ]
            if value
        )

        story.append(
            Paragraph(links, contact_style)
        )

    sections = [
        ("PROFESSIONAL SUMMARY", resume["summary"]),
        ("EDUCATION", resume["education"]),
        ("SKILLS", resume["skills"]),
        ("EXPERIENCE", resume["experience"]),
        ("PROJECTS", resume["projects"]),
        ("CERTIFICATIONS", resume["certifications"]),
        ("ACHIEVEMENTS", resume["achievements"])
    ]

    for title, content in sections:

        if content:

            story.append(
                Paragraph(title, heading_style)
            )

            story.append(
                HRFlowable(
                    width="100%",
                    thickness=0.5,
                    color=colors.grey
                )
            )

            formatted_content = content.replace(
                "\n",
                "<br/>"
            )

            story.append(
                Paragraph(
                    formatted_content,
                    normal_style
                )
            )

            story.append(Spacer(1, 5))

    document.build(story)

    return file_path