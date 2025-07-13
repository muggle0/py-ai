from zhipuai import ZhipuAI

if __name__ == '__main__':
    ai = ZhipuAI(api_key="xxxx")
    ai.chat.completions.create(model="glm-4", messages=[{"role": "user", "content": "prompt"}])
