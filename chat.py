"""
迷你向量库命令行交互界面
"""
from minivectordb import MiniVectorDB

print("="*50)
print("迷你本地向量检索引擎 v0.1")
print("输入问题回车检索，输入q退出")
print("="*50)

db = MiniVectorDB(storage_file="408_vectordb.json")

while True:
    q = input("\n你的问题：").strip()
    if q.lower() == "q":
        break
    if not q:
        continue
    results = db.search(q, top_k=2)
    print("\n检索到的最相关知识点：")
    for i, (doc, score) in enumerate(results):
        print(f"\n--- 匹配{i+1}（相似度{score:.3f}） ---")
        print(doc[:200])
