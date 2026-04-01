from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import date

from backend import models
from backend.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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