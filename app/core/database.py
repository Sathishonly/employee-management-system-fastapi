from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from app.core.config import DATABASE_URL


Engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=Engine,autoflush=False)

Base = declarative_base()

def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()