from pydantic import BaseModel, Field

# やりたいことをコメントアウトで書いていく
# クライアント（Reactなど）から「送られてくる」データの型を厳格に定義
class RecordCreate(BaseModel):
    action: str = Field(..., example="study", description="行った行動")
    emotion_score: int = Field(..., ge=0, le=100, description="感情スコア(0~100)")
    # ※ ge=0, le=100 と書くことで、「0未満、100より大きい数字が来たら自動で弾く」という強力なバリデーションが働きます！

# 2. クライアントへ「返す」データの型を厳格に定義
class RecordResponse(BaseModel):
    id: int
    action: str
    emotion_score: int

    # これを書くことで、SQLAlchemyのモデル（DBのデータ）を
    # 自動的にこのPydanticの型に変換してくれます（超便利！）
    class Config:
        from_attributes = True