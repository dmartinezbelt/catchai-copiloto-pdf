from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend import pdf_loader # Importa el router de pdf_loader

# -----------------------------
# Crear la aplicación FastAPI
# -----------------------------
app = FastAPI(
    title="CatchAI Copilot API",
    description="Backend para manejar carga y procsamiento de PDFs",
    version="0.1.0",
    )

# -----------------------------
# Configurar CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar a la URL del frontend en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Montar routers
# -----------------------------
app.include_router(pdf_loader.router, prefix="/pdf", tags=["PDF Handling"])

# -----------------------------
# Endpoint de prueba
# -----------------------------
@app.get("/")
async def root():
    return {"message": "API de CatchAI Copiloto PDF en funcionamiento"}