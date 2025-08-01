import os

from langchain.chat_models import init_chat_model
from langchain_community.tools import TavilySearchResults
from torch.onnx import export

if __name__ == '__main__':
    # os.environ["TAVILY_API_KEY"] = "my_value"
    # results = TavilySearchResults(max_results=1,tavily_api_key="xx",)
    # print(results.invoke("肉包的做法"))
    model = init_chat_model(
        model="deepseek-r1:8b",  # 模型名称
        model_provider="openai",
        base_url="https://api.deepseek.com/v1",  # 硅基流动模型的请求url
        api_key="x",  # 填写你注册的硅基流动 API Key
    )