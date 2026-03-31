from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Worker data model
class Worker(BaseModel):
    name: str
    phone: str
    skill: str
    daily_rate: float

# Temporary storage (we'll connect database later)
workers = []

@app.get("/")
def home():
    return {"message": "Construction Payroll API is running"}

@app.post("/workers")
def add_worker(worker: Worker):
    workers.append(worker)
    return {"message": "Worker added successfully", "worker": worker}

@app.get("/workers")
def get_workers():
    return workers