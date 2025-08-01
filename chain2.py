from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
def debug_print(x):
    print('中间结果：', x)
    return x

if __name__ == '__main__':
    # 第一步：根据标题生成新闻正文
    cook_prompt = PromptTemplate.from_template(
        "请根据菜品名给出做菜的步骤：\n\n菜品名：{title}"
    )
    model = ChatOpenAI(api_key="sk-e3cb8a78bd54403eb488390565ece237", base_url="https://api.deepseek.com/v1",
                       model="deepseek-chat")
    # 第一个子链：做菜步骤
    cook_chain = cook_prompt | model

    # 第二步：从正文中提取结构化字段
    schemas = [
        ResponseSchema(name="material", description="食材"),
        ResponseSchema(name="flavoring", description="调味料"),
    ]
    parser = StructuredOutputParser.from_response_schemas(schemas)

    summary_prompt = PromptTemplate.from_template(
        "请从下面这段内容中提取关键信息，并返回结构化JSON格式：\n\n{msg}\n\n{format_instructions}"
    )
    print(parser.get_format_instructions())
    # 输出中间结果
    debug_node = RunnableLambda(debug_print)
    # 第二个子链：生成新闻摘要
    summary_chain = (
            summary_prompt.partial(format_instructions=parser.get_format_instructions())
            | model
            | parser
    )

    # 组合成一个复合 Chain
    full_chain = cook_chain | debug_node | summary_chain

    # 调用复合链
    result = full_chain.invoke({"title": "蛋炒饭"})
    print(result)
