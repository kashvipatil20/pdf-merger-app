# 📄 PDF Merger App

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green.svg)
![Status](https://img.shields.io/badge/Status-Deployed-success)

A lightweight web application built with **FastAPI** that allows users to upload multiple PDF files and merge them into a single downloadable document.

---

## 🚀 Live Demo

🔗 https://pdf-merger-app-slph.onrender.com/

---

## 📌 Features

- Upload multiple PDF files at once  
- Merge PDFs into a single file instantly  
- Download merged output  
- Simple and clean UI  
- FastAPI backend with minimal latency  
- Temporary file handling for uploads  

---

## 🧠 Tech Stack

- **Backend:** FastAPI, Python  
- **Server:** Uvicorn  
- **Frontend:** HTML, CSS (Jinja2 templates)  
- **Deployment:** Render  

---

## 🏗️ Project Structure

pdf-merger-app/
│
├── main.py # FastAPI backend logic
├── templates/ # HTML templates (UI)
├── static/ # CSS / JS (if any)
├── uploads/ # Temporary uploaded PDFs
├── merged/ # Output merged PDFs
├── venv/ # Virtual environment (not pushed to GitHub)
├── requirements.txt # Dependencies
└── README.md

---

## ⚙️ Installation (Run Locally)

```bash
# Clone repository
git clone https://github.com/kashvipatil20/pdf-merger-app.git

# Move into directory
cd pdf-merger-app

# Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
