import openai
import os

# 尝试从环境变量读取 DEEPSEEK_API_KEY
api_key = os.environ.get('DEEPSEEK_API_KEY')

if api_key:
    print('API 配置已就绪')
else:
    print('请配置 API Key')
