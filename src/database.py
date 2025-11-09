from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DatabaseConfig

engine = create_engine(DatabaseConfig.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class DatabaseManager:
    def __init__(self):
        self.engine = engine
        
    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)
        
    def get_session(self):
        return SessionLocal()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()