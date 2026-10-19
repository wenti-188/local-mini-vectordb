"""
测试脚本：导入408知识点，验证我们自己写的向量检索效果
"""
import os
from minivectordb import MiniVectorDB

# 读取之前RAG项目里的408知识点文件
knowledge_dir = r"C:\项目\rag-408-project\knowledge"
all_texts = []
for filename in os.listdir(knowledge_dir):
    if filename.endswith(".md"):
        with open(os.path.join(knowledge_dir, filename), "r", encoding="utf-8") as f:
            content = f.read()
            # 按段落切分文本
            paragraphs = [p.strip() for p in content.split("\n\n") if len(p.strip()) > 20]
            all_texts.extend(paragraphs)

print(f"共读取到 {len(all_texts)} 个知识段落")

# 初始化我们自己的迷你向量库
db = MiniVectorDB(storage_file="408_vectordb.json")

# 如果库是空的，就导入知识点
if len(db.documents) == 0:
    db.add_texts(all_texts)
    db.save()

# 测试搜索几个典型问题
test_questions = [
    "TCP三次握手的过程是什么？",
    "进程调度有哪些常见算法？",
    "什么是栈？它的特点是什么？"
]

for q in test_questions:
    print(f"\n===== 问题：{q} =====")
    results = db.search(q, top_k=2)
    for i, (doc, score) in enumerate(results):
        print(f"匹配{i+1}（相似度{score:.3f}）：{doc[:100]}...")
