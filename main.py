from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
import os
from dotenv import load_dotenv

load_dotenv('.env')

SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    action = Column(String, index=True)
    emotion_score = Column(Integer)

Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message":"Hello to the WSL CLI"}

# 自分のトラッカ用お試しAPI(POSTリクエスト)
@app.post("/tracker")
def creat_record(action: str, emotion_score: int, db: Session = Depends(get_db)):

    new_record = Record(action=action, emotion_score=emotion_score)

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return {
        'status': "success",
        'data':new_record
    }

@app.get("/tracker")
def read_records(db: Session = Depends(get_db)):
    records = db.query(Record).all()

    return records