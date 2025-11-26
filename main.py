# File: main.py

import tkinter as tk
from tkinter import filedialog, messagebox
import docx
import pdfplumber

def extract_text(file_path):
    if file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        full_text = "\n".join([para.text for para in doc.paragraphs])
        return full_text
    elif file_path.endswith('.pdf'):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
    else:
        messagebox.showerror("Error", "Unsupported file format!")
        return ""

def suggest_career(resume_text):
    resume_text = resume_text.lower()
    if "python" in resume_text or "programming" in resume_text or "data" in resume_text:
        return "Suggested Careers: Software Developer, Data Scientist, AI Engineer"
    elif "marketing" in resume_text or "sales" in resume_text:
        return "Suggested Careers: Marketing Manager, Sales Analyst"
    elif "design" in resume_text or "creative" in resume_text:
        return "Suggested Careers: Graphic Designer, UI/UX Designer"
    elif "research" in resume_text or "science" in resume_text:
        return "Suggested Careers: Research Scientist, Lab Technician"
    else:
        return "Suggested Careers: General Career Counselor Advice Needed"

def upload_resume():
    file_path = filedialog.askopenfilename(
        title="Select Resume",
        filetypes=(("Word files", "*.docx"), ("PDF files", "*.pdf"))
    )
    if file_path:
        resume_text = extract_text(file_path)
        career = suggest_career(resume_text)
        result_label.config(text=career)

root = tk.Tk()
root.title("AI Career Path Advisor")
root.geometry("500x300")

label = tk.Label(root, text="Upload your resume to get career suggestions", font=("Arial", 14))
label.pack(pady=20)

upload_button = tk.Button(root, text="Upload Resume", command=upload_resume, font=("Arial", 12))
upload_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=400, justify="center")
result_label.pack(pady=20)

root.mainloop()
