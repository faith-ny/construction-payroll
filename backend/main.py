from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from fastapi.responses import StreamingResponse
import csv
import io


app = FastAPI()

# ---------------------------
# Models
# ---------------------------
class Worker(BaseModel):
    name: str
    phone: str
    skill: str
    daily_rate: float

class Attendance(BaseModel):
    worker_id: int
    date: date
    status: str  # present or absent

workers = []
attendance_records = []

# ---------------------------
# Home
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
    return {"message": "Worker added", "worker": worker}

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

@app.get("/attendance/{worker_id}")
def get_worker_attendance(worker_id: int):
    return [r for r in attendance_records if r.worker_id == worker_id]

# ---------------------------
# Payroll Endpoint
# ---------------------------

@app.get("/payroll/export")
def export_payroll():
    output = io.StringIO()
    writer = csv.writer(output)

    # CSV header
    writer.writerow(["Worker ID", "Name", "Days Present", "Daily Rate", "Total Pay"])

    for worker_id, worker in enumerate(workers):
        days_present = sum(
            1 for r in attendance_records
            if r.worker_id == worker_id and r.status == "present"
        )

        total_pay = days_present * worker.daily_rate

        writer.writerow([
            worker_id,
            worker.name,
            days_present,
            worker.daily_rate,
            total_pay
        ])

    output.seek(0)

    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=payroll_report.csv"}
    )

@app.get("/payroll/{worker_id}")
def calculate_payroll(worker_id: int):
    if worker_id >= len(workers):
        return {"error": "Worker not found"}

    worker = workers[worker_id]

    days_present = sum(
        1 for r in attendance_records
        if r.worker_id == worker_id and r.status == "present"
    )

    total_pay = days_present * worker.daily_rate

    return {
        "worker": worker.name,
        "days_present": days_present,
        "daily_rate": worker.daily_rate,
        "total_pay": total_pay
    }

@app.get("/payroll")
def calculate_all_payroll():
    payroll_list = []

    for worker_id, worker in enumerate(workers):
        days_present = sum(
            1 for r in attendance_records
            if r.worker_id == worker_id and r.status == "present"
        )

        total_pay = days_present * worker.daily_rate

        payroll_list.append({
            "worker_id": worker_id,
            "name": worker.name,
            "days_present": days_present,
            "daily_rate": worker.daily_rate,
            "total_pay": total_pay
        })

    return payroll_list

