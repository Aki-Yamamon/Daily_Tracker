// frontend/src/App.tsx
import { useState } from 'react'

function App() {
  // 画面の入力値やデータを覚えておくための「状態（State）」
  const [action, setAction] = useState("")
  const [score, setScore] = useState(50)
  const [records, setRecords] = useState<any[]>([]) // 取得したデータを保存する配列

  // --- POST通信（データを送信して保存する） ---
  const handleSubmit = async () => {
    // FastAPIに送るデータを、スキーマと同じJSONの形にまとめる
    const payload = {
      action: action,
      emotion_score: score
    }

    // fetchを使って、FastAPIの /addscore にPOST通信を送る！
    const response = await fetch("http://127.0.0.1:8000/addscore", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (response.ok) {
      alert("保存に成功しました！")
      // 保存に成功したら、最新のデータを取得し直す
      handleGetRecords()
    } else {
      alert("エラーが発生しました")
    }
  }

  // --- GET通信（データの一覧を取得する） ---
  const handleGetRecords = async () => {
    const response = await fetch("http://127.0.0.1:8000/scores")
    const data = await response.json()
    setRecords(data) // 取得したデータを状態にセットして画面を更新する
  }

  return (
    <div style={{ padding: "20px", fontFamily: "sans-serif" }}>
      <h1>日々のトラッカー (動くゴミ版)</h1>

      {/* 入力フォーム */}
      <div style={{ marginBottom: "20px", border: "1px solid #ccc", padding: "10px" }}>
        <h3>新しい記録を追加</h3>
        <p>行動: <input type="text" value={action} onChange={(e) => setAction(e.target.value)} /></p>
        <p>感情スコア: <input type="number" value={score} onChange={(e) => setScore(Number(e.target.value))} /></p>
        <button onClick={handleSubmit} style={{ padding: "10px", background: "blue", color: "white" }}>
          保存する！
        </button>
      </div>

      {/* データ表示エリア */}
      <div>
        <button onClick={handleGetRecords} style={{ padding: "10px", marginBottom: "10px" }}>
          データをDBから取得する
        </button>
        <ul>
          {/* recordsの配列をぐるぐる回してリスト表示する */}
          {records.map((record, index) => (
            <li key={index}>
              ID: {record.id} | 行動: {record.action} | スコア: {record.emotion_score}
            </li>
          ))}
        </ul>
      </div>
    </div>
  )
}

export default App