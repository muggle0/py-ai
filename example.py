from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings, OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

#  示例筛选与运用
if __name__ == '__main__':
    examples: dict[str, str] =[ {"question": "秦始皇和孔子谁的寿命更长", "answer": """
    孔子的寿命更长。

    秦始皇嬴政生于公元前 259 年，逝于公元前 210 年，终年 50 岁。孔子约生于公元前 551 年，逝于公元前 479 年，享年 73 岁。相比之下，孔子比秦始皇寿命长 23 岁。"""},
                                {"question": "周杰伦多少岁了", "answer": "根据公开资料，周杰伦出生于1979年1月18日‌截至2025年7月29日，他的年龄为：46周岁‌"}]
    # print(examples["question"])
    # 问答样例
    example_prompt = PromptTemplate(input_variables=["question", "answer"], template="问题：{question}\\n{answer}")
    # print(example_prompt.format(**examples[0]))
    prompt = FewShotPromptTemplate(
        examples = examples,
        example_prompt = example_prompt,
        suffix = "问题:{input}", input_variables = ["input"]
    )
    print(prompt.format(input="周杰伦多少岁了"))
    embeddings = OllamaEmbeddings(
     # 本地模型地址
        model="deepseek-r1:8b"
    )
    example_selector = SemanticSimilarityExampleSelector.from_examples(
        # 这是可供选择的示例列表。
        examples,
        # 用于衡量语义相似性。
        embeddings,
    # 这是用于存储嵌入和执行相似性搜索的vectorstore类。
        Chroma,
    # 这是要生成的示例数。
    k=1)
    question="周杰伦多少岁"
    selected_examples = example_selector.select_examples({"question": question})
    for selected_example in selected_examples:
        print(selected_example)

    # print(example_prompt.format(**examples[0]))
    prompt_next = FewShotPromptTemplate(
        example_selector = example_selector,
        example_prompt=example_prompt,
        suffix="问题:{input}", input_variables=["input"]
    )
    next_format = prompt_next.format(input=question)
    print(prompt_next.format(input=question))
    # ChatPromptTemplate.format_messages(examples)
    # print(example_prompt.format(**examples[0]))
    # print()
    # 使用语义相似性示例选择器 Chroma 开源向量数据库 OpenAIEmbeddings 数据转化成向量

    # selector_from_examples = SemanticSimilarityExampleSelector.from_examples(examples, OpenAIEmbeddings(api_key="sk-e3cb8a78bd54403eb488390565ece237",base_url="https://api.deepseek.com/v1",model="deepseek-chat"), Chroma, k=1)
    # select_examples = selector_from_examples.select_examples({"question", "秦始皇和孔子谁的寿命更长"})
    # for example in select_examples:
    #     for k, v in enumerate(example):
    #         print(example[k], v)
