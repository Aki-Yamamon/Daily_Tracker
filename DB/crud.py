from sqlalchemy.orm import Session
import models
import schemas as schemas

# --- Read --- データの取得する関数 (すべてのデータ)
def get_records(db: Session):

    return db.query(models.Record).all()


# --- Create --- データを作成する関数
def create_record(db: Session, record: schemas.RecordCreate):
    db_record = models.Record(
        action=record.action,
        emotion_score=record.emotion_score
    )

    # dbへのデータ書き込み
    db.add(db_record)
    db.commit()
    db.refresh(db_record)

    return db_record