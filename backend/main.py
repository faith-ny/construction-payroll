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