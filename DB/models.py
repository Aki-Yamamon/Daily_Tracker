from sqlalchemy import Column, Integer, String
# クラスをインポート
from database import Base 

# DBの設定
class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)

    # --- オリジナルカラム ---
    action = Column(String, String, index=True)
    emotion_score = Column(Integer)