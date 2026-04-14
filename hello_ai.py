import os
from openai import OpenAI

# 1. 初始化客户端 (这里会直接读取你刚才设的系统环境变量)
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"), 
    base_url="https://api.deepseek.com" # 如果你用的是 DeepSeek
)

# 2. 发起对话
try:
    print("正在连接 AI 脑回路...")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system", 
                "content": "你现在是一名极其严苛的硅谷大厂架构师。你说话简短、刻薄但极其专业。你只用代码说话，如果对方的代码写得烂，你会毫不留情地指出。"
            },
            {
                "role": "user", 
                "content": "作为架构师，既然你觉得我的代码太嫩，请给我布置一个 Python 进阶挑战题。\n要求：\n必须使用今天安装的 openai 库。\n题目要涉及：如何让 AI 总结一个本地 .txt 文件里的内容（这就是 RAG 的雏形）。\n请给出明确的输入、输出要求，但不要直接给我答案。"
            }
        ],
        stream=False
    )

    # 3. 打印结果
    print("\nAI 回复：")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"\n[no] 报错了，别慌，这是排查清单：\n{e}")