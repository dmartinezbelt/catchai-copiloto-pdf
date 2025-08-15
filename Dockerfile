# Imagen base de Python
FROM python:3.10-slim

# Configuración del directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de requerimientos
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Exponer puertos (Streamlit: 8501, FastAPI: 8000)
EXPOSE 8501
EXPOSE 8000

# Comando por defecto (solo ejemplo para desarrollo)
CMD ["streamlit", "run", "frontend/app.py", "--server.port=8501", "--server.address=0.0.0.0"]