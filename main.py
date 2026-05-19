from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from pypdf import PdfWriter
import os
import uuid

app = FastAPI()

templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
MERGED_DIR = "merged"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(MERGED_DIR, exist_ok=True)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/merge")
async def merge_pdfs(files: list[UploadFile] = File(...)):

    merger = PdfWriter()

    temp_files = []

    for file in files:
        file_path = os.path.join(
            UPLOAD_DIR,
            f"{uuid.uuid4()}.pdf"
        )

        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        temp_files.append(file_path)

    for pdf in temp_files:
        merger.append(pdf)

    merged_filename = f"merged_{uuid.uuid4()}.pdf"
    merged_path = os.path.join(MERGED_DIR, merged_filename)

    merger.write(merged_path)
    merger.close()

    return FileResponse(
        merged_path,
        media_type="application/pdf",
        filename="merged.pdf"
    )