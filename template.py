from langchain_core.prompts import ChatPromptTemplate

if __name__ == "__main__":
    chat_template =ChatPromptTemplate.from_messages([
        ("system","你是一位人工智能助手，你的名字是{name}。"),
        ("human","你好"),
        ("ai","我很好，谢谢!"),
        ("human", "{input}")
    ])

    #通过模板参数格式化模板内容1718
    messages = chat_template.format_messages(name="小度",input="你的名字叫什么");
    print(messages)