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
            {"role": "system", "content": "你是一个资深的程序员导师。"},
            {"role": "user", "content": "你好，我是 Li-Agent-Explorer，我刚刚配置好了开发环境，请给我一句鼓励。"}
        ],
        stream=False
    )

    # 3. 打印结果
    print("\nAI 回复：")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"\n[no] 报错了，别慌，这是排查清单：\n{e}")