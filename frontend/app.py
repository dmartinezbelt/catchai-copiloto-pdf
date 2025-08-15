import streamlit as st
import requests
import os

# -----------------------------
# Configuración de la app
# -----------------------------

st.set_page_config(
    page_title="CatchAI Copiloto PDF",
    layout="wide"
    )

# -----------------------------
# Título de la app
# -----------------------------
st.title("CatchAI Copilot")

# -----------------------------
# Subida de PDFs (Frontend)
# -----------------------------
# TODO: Implementar la funcionalidad de subida de PDFs y envío al backend
uploaded_files = st.file_uploader(
    "Sube hasta 5 PDFs",
    type=["pdf"],
    accept_multiple_files=True
)
if st.button("Subir PDFs"):
    if uploaded_files:
        files_to_send = [("files", (f.name, f, "application/pdf")) for f in uploaded_files]
        response = requests.post("http://backend:8000/pdf/upload-pdfs", files=files_to_send)
        st.write(response.json())
    else:
        st.warning("Por favor, sube al menos un PDF.")

# Ejemplo de boton para enviar PDFs al backend
if st.button("Procesar PDFs"):
    st.write("Procesando PDFs... (esta funcionalidad aún no está implementada)")

# -----------------------------
# Chat Interface Placeholder
# -----------------------------
# TODO: Implementar la interfaz de chat
st.subheader("Chat (Placeholder)")
user_input = st.text_input("Escribe tu pregunta aquí...")
if user_input:
    st.write("Respuesta pendiente de implementación...")
st.write("Frontend is running!")