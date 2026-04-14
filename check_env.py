import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 读取刚才定义的变量
secret_val = os.getenv("MY_SECRET_TEST")

print("--- 环境变量检测 ---")
if secret_val:
    print(f"[ok] 成功读取到变量内容: {secret_val}")
    print("结论：你的‘保险柜’配置完全正确，明天可以安全存放 API Key 了。")
else:
    print("[error] 读取失败，请检查 .env 文件名及内容格式。")