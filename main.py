from fastapi import FastAPI

#FastAPIのインスタンスを作成する
app = FastAPI()

# 「http://.../」にGET通信が来たら、下の関数を実行するという名札（デコレータ）
@app.get("/")
def read_root():
    return {"message":"Hello, Tracker App!"}

# 自分のトラッカ用お試しAPI(POSTリクエスト)
@app.post("/tracker")
def creat_record(action: str, emotion_score: int):
    return {
            "status": "success",
            "action_received": action,
            "emotion": emotion_score
            }

