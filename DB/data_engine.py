import sqlite3
import numpy as np
import matplotlib.pyplot as plt
# import matplotlibe.pyplot as plt
import pandas as pd

conn = sqlite3.connect("tracker.db")

df = pd.read_sql_query("SELECT action, emotion_score FROM records", conn)
conn.close()


scores_array = df['emotion_score'].to_numpy()

print(f"データの個数: {len(scores_array)}")
print(f"感情スコアの標準偏差: {scores_array}")

mean_score = np.mean(scores_array)
std_dev = np.std(scores_array)
print(f"感情スコアの平均: {mean_score:.2f}")
print(f"感情スコアの標準偏差: {std_dev:.2f}")


plt.figure(figsize=(8, 5))

plt.hist(scores_array, bins=10, color='skyblue', edgecolor='black', alpha=0.7)

plt.axvline(mean_score, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_score:.1f}')

plt.title('Distribution of Emotion Scores')
plt.xlabel('Emotion Score')
plt.ylabel('Frequency')
plt.legend()
plt.grid(axis='y', alpha=0.75)

# 画像として保存（この画像を後々Webアプリで表示させます）
plt.savefig('emotion_distribution.png')
print("分析グラフを emotion_distribution.png として保存しました！")
