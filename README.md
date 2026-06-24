Daily_Tracker/
 ├── database.py   # DBのエンジンやセッション設定（接続インフラ）
 ├── models.py     # SQLAlchemyのモデル（DBのテーブル設計図）
 ├── schemas.py    # Pydanticのスキーマ（APIの入出力の「型」の設計図）★最重要
 ├── crud.py       # DBを操作する関数群（Create, Read, Update, Delete）
 └── main.py       # APIのエンドポイント（URLの受け口）だけを書く場所
