skills = {
    "Python": "Environment Ready",
    "RAG": "Concept Known",
    "Agent": "Concept Known",
    "LangChain": "Concept Known"
}

print("--- Day 1 技能盘点 ---")
for skill, status in skills.items():
    if status == "Environment Ready":
        print(f"[OK] {skill}: 环境已就绪")
    else:
        print(f"[PEND] {skill}: 理论已了解，待实战")