from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import date

try:
    # Works when launched from project root: uvicorn backend.main:app --reload
    from backend import models
    from backend.database import SessionLocal, engine
except ModuleNotFoundError:
    # Works when launched from backend folder: uvicorn main:app --reload
    import models
    from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1):\d+",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# Database Dependency
# ---------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------------
# Pydantic Schemas
# ---------------------------
class WorkerCreate(BaseModel):
    name: str
    phone: str
    skill: str
    daily_rate: float

class AttendanceCreate(BaseModel):
    worker_id: int
    date: date
    status: str

# ---------------------------
# Worker Endpoints
# ---------------------------
@app.post("/workers")
def add_worker(worker: WorkerCreate, db: Session = Depends(get_db)):
    db_worker = models.Worker(**worker.dict())
    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)
    return db_worker

@app.get("/workers")
def get_workers(db: Session = Depends(get_db)):
    return db.query(models.Worker).all()

# ---------------------------
# Attendance Endpoints
# ---------------------------
@app.post("/attendance")
def mark_attendance(record: AttendanceCreate, db: Session = Depends(get_db)):
    db_record = models.Attendance(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

@app.get("/attendance")
def get_all_attendance(db: Session = Depends(get_db)):
    return db.query(models.Attendance).all()

@app.get("/attendance/{worker_id}")
def get_worker_attendance(worker_id: int, db: Session = Depends(get_db)):
    return db.query(models.Attendance).filter(
        models.Attendance.worker_id == worker_id
    ).all()

# ---------------------------
# Payroll Endpoints (DB-based)
# ---------------------------
@app.get("/payroll/{worker_id}")
def calculate_payroll(worker_id: int, db: Session = Depends(get_db)):
    worker = db.query(models.Worker).filter(
        models.Worker.id == worker_id
    ).first()

    if not worker:
        return {"error": "Worker not found"}

    days_present = db.query(models.Attendance).filter(
        models.Attendance.worker_id == worker_id,
        models.Attendance.status == "present"
    ).count()

    total_pay = days_present * worker.daily_rate

    return {
        "worker_id": worker.id,
        "name": worker.name,
        "days_present": days_present,
        "daily_rate": worker.daily_rate,
        "total_pay": total_pay
    }


@app.get("/payroll")
def calculate_all_payroll(db: Session = Depends(get_db)):
    workers = db.query(models.Worker).all()
    payroll_list = []

    for worker in workers:
        days_present = db.query(models.Attendance).filter(
            models.Attendance.worker_id == worker.id,
            models.Attendance.status == "present"
        ).count()

        total_pay = days_present * worker.daily_rate

        payroll_list.append({
            "worker_id": worker.id,
            "name": worker.name,
            "days_present": days_present,
            "daily_rate": worker.daily_rate,
            "total_pay": total_pay
        })

    return payroll_list