from fastapi import FasetAPI, Depends, BackgroundTasks
from fastapi.responses import FileResponse # ファイルを返すための機能


app = FasetAPI

# root とりあえず確認用
@app.get("/")
def test_root():
    return {
        "success": "from new main.py to Hallo"
    }

# レコード (テーブル？)新規作成API
# @app.post("/addscore")
# def 

# @app.get("")