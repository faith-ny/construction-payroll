from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
try:
    # Works when launched from project root
    from backend.database import Base
except ModuleNotFoundError:
    # Works when launched from backend folder
    from database import Base

class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    skill = Column(String)
    daily_rate = Column(Float)


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("workers.id"))
    date = Column(Date)
    status = Column(String)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("workers.id"))
    amount = Column(Float)
    method = Column(String)  # cash / openfloat / boya
    date = Column(Date)