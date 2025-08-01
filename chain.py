from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

if __name__ == '__main__':
    model = ChatOpenAI(api_key="x", base_url="https://api.deepseek.com/v1", model="deepseek-chat")

    # 搭建链条，把model和字符串输出解析器组件连接在一起
    basic_qa_chain = model | StrOutputParser()

    # 查看输出结果
    question = "周杰伦的青花瓷第一句歌词是什么"
    result = basic_qa_chain.invoke(question)
    print(result)

    prompt_template = ChatPromptTemplate([
        ("system", "你是一位人工智能助手，你的名字是{name}"),
        ("user", "这是用户的问题： {question}")
    ])

    # 直接使用模型 + 输出解析器
    bool_qa_chain = prompt_template | model | StrOutputParser()
    # 测试
    question = "你叫什么名字"
    result = bool_qa_chain.invoke({'question':question,"name":"机器人"})
    print(result)
