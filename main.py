from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session


# DBフォルダの中から必要なものをインポート
from DB import crud, schemas, models
from DB.database import SessionLocal, engine

app = FastAPI()

# --- CORSの設定（これがないとReactから通信できない！） ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 本当は ["http://localhost:3000"] のように指定するが、今は全部許可
    allow_credentials=True,
    allow_methods=["*"], # GET, POST, PUT, DELETEなど全部許可
    allow_headers=["*"], # すべてのヘッダーを許可
)

# データベースのテーブルを実際に作成する
models.Base.metadata.create_all(bind=engine)

# データベースのセッション（ウェイター）を呼んで、終わったら閉じる関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# root とりあえず確認用
@app.get("/")
def test_root():
    return {
        "success": "from new main.py to Hallo"
    }

    # --- Create ---
@app.post("/addscore", response_model=schemas.RecordResponse)
def addscore(record: schemas.RecordCreate, db: Session = Depends(get_db)):
    # ユーザーから受け取った record (安全な箱) を、そのまま crud に丸投げ！
    return crud.create_record(db=db, record=record)

# --- Read --- (これも追加しましょう！)
@app.get("/scores", response_model=list[schemas.RecordResponse])
def get_scores(db: Session = Depends(get_db)):
    # crudに「全部取ってきて」とお願いして返すだけ！
    return crud.get_records(db=db)