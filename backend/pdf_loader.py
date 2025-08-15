import os
import hashlib
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List

# Dependencias de PDF
import pypdf
import pdfplumber

# -----------------------------
# Configuración
# -----------------------------
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

router = APIRouter()
MAX_FILES = 5

# -----------------------------
# Endpoint: Subir y procesar PDFs
# -----------------------------
@router.post("/upload-pdfs")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    # Validar número de archivos, no puede ser más de 5
    if len(files) > MAX_FILES:
        raise HTTPException(status_code=400, detail=f"Solo se permiten hasta {MAX_FILES} archivos PDF")
    
    seen_hashes = set()
    seen_filenames = set()
    saved_files = []

    # Validar que sean PDF
    for file in files:
        if file.content_type != "application/pdf":
            raise HTTPException(status_code=400, detail="Todos los archivos deben ser PDFs")
        
        # Leer el contenido solo una vez
        content = await file.read()
        
        # Evitar archivos duplicados por contenido
        file_hash = hashlib.sha256(content).hexdigest()
        if file_hash in seen_hashes:
            raise HTTPException(status_code=400, detail=f"Archivo duplicado: {file.filename}")
        seen_hashes.add(file_hash)

        # Validar que no haya archivos con el mismo nombre para evitar conflictos
        if file.filename in seen_filenames:
            raise HTTPException(status_code=400, detail=f"El archivo {file.filename} ya existe")
        seen_filenames.add(file.filename)

        # Generar un nombre único para cada archivo
        unique_name = f"{uuid.uuid4()}_{file.filename}.pdf"
        save_path = os.path.join(UPLOAD_DIR, unique_name)
       
        # Guardar el archivo en el servidor
        with open(save_path, "wb") as f:
            f.write(content)

        saved_files.append(unique_name)
    
    return {"uploaded_files": saved_files, "message": "Archivos subidos correctamente"}
    
    # Validar que no haya archivos con el mismo nombre en la misma subida
    # Esto es para evitar conflictos si se suben varios archivos con el mismo nombre

# -----------------------------
# Función: Extraer texto de PDF
# -----------------------------
def extract_text_from_pdf(file_path: str) -> str:
    # TODO: Implementar la extracción de texto con pypdf, fallback pdfplumber si es necesario
    return ""