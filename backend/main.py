from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

# Worker Model
# ---------------------------
class Worker(BaseModel):
    name: str
    phone: str
    skill: str
    daily_rate: float

workers = []

# ---------------------------
# Attendance Model
# ---------------------------
class Attendance(BaseModel):
    worker_id: int
    date: date
    status: str  # present, absent

attendance_records = []

# ---------------------------
# Routes
# ---------------------------
@app.get("/")
def home():
    return {"message": "Construction Payroll API is running"}

# ---------------------------
# Worker Endpoints
# ---------------------------
@app.post("/workers")
def add_worker(worker: Worker):
    workers.append(worker)
    return {"message": "Worker added successfully", "worker": worker}

@app.get("/workers")
def get_workers():
    return workers

# ---------------------------
# Attendance Endpoints
# ---------------------------
@app.post("/attendance")
def mark_attendance(record: Attendance):
    attendance_records.append(record)
    return {"message": "Attendance recorded", "record": record}

@app.get("/attendance")
def get_all_attendance():
    return attendance_records

@app.get("/attendance/{worker_id}")
def get_worker_attendance(worker_id: int):
    worker_logs = [r for r in attendance_records if r.worker_id == worker_id]
    return worker_logs