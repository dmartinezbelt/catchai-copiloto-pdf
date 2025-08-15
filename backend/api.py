from fastapi import FastAPI

app = FastAPI(title="CatchAI Copilot API")

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}