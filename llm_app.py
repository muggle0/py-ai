# 聊天提示模板
# from av.container import result
from langchain.chains.question_answering.map_rerank_prompt import output_parser
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from langchain_openai import ChatOpenAI

if __name__ == '__main__':
    llm = ChatOpenAI(api_key="",base_url="https://api.deepseek.com/v1",model="deepseek-chat")
    prompt = ChatPromptTemplate.from_template("请根据提示词生成营销短文：{input}")
    output_parser=StrOutputParser()
    # 自定义操作符重载
    chain = prompt | llm | output_parser # 使用管道操作符替代旧版 LLMChain
    # print(chain.invoke({"input":"康师傅绿茶"}))
    for chunk in chain.stream({"input": "康师傅绿茶"}):
        print(chunk, end="", flush=True)
