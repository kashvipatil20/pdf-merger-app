# 📄 PDF Merger App

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green.svg)
![Status](https://img.shields.io/badge/Status-Deployed-success)

A lightweight web application built with **FastAPI** that allows users to upload multiple PDF files and merge them into a single downloadable document.

---

## 🚀 Live Demo

🔗 [https://pdf-merger-app-slph.onrender.com/](https://pdf-merger-app-slph.onrender.com/)

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
├── main.py            # FastAPI backend logic
├── templates/         # HTML templates (UI)
├── static/            # CSS / JS files
├── uploads/           # Temporary uploaded PDFs
├── merged/            # Output merged PDFs
├── requirements.txt   # Dependencies
└── README.md

---

## ⚙️ Installation (Run Locally)

```bash
git clone https://github.com/kashvipatil20/pdf-merger-app.git
cd pdf-merger-app
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
uvicorn main:app --reload
```

Open your browser and go to `http://127.0.0.1:8000`

---

## 📡 API Endpoints

| Method | Endpoint | Description           |
|--------|----------|-----------------------|
| GET    | `/`      | Home page             |
| POST   | `/merge` | Upload and merge PDFs |

---

## 📸 How It Works

1. Upload multiple PDF files via the web UI
2. Backend processes and merges the files using FastAPI
3. Merged PDF is generated and ready for download
4. Download the merged output instantly

---

## 🌍 Deployment

Deployed live on Render:
🔗 [https://pdf-merger-app-slph.onrender.com/](https://pdf-merger-app-slph.onrender.com/)

To deploy your own:
1. Fork this repo
2. Create a new Web Service on [Render](https://render.com/)
3. Set the start command to: `uvicorn main:app --host 0.0.0.0 --port 10000`
4. Deploy!

---

## 👨‍💻 Author

**Kashvi Patil**  
GitHub: [@kashvipatil20](https://github.com/kashvipatil20)
