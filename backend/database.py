from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Always use the DB next to this file, not the process cwd (avoids multiple empty DBs).
_BACKEND_DIR = Path(__file__).resolve().parent
_DB_FILE = _BACKEND_DIR / "construction_payroll.db"
DATABASE_URL = f"sqlite:///{_DB_FILE.as_posix()}"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()