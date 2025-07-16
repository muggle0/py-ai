from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import OpenAIEmbeddings

#  示例筛选与运用
if __name__ == '__main__':
    examples: dict[str, str] =[ {"question": "秦始皇和孔子谁的寿命更长", "answer": """
    孔子的寿命更长。

    秦始皇嬴政生于公元前 259 年，逝于公元前 210 年，终年 50 岁。孔子约生于公元前 551 年，逝于公元前 479 年，享年 73 岁。相比之下，孔子比秦始皇寿命长 23 岁。"""}]
    # print(examples["question"])
    # 问答样例 变量命名快捷键 ctl+alt+v
    example_prompt = PromptTemplate(input_variables=["question", "answer"], template="问题：{question}\\n{answer}")
    # prompt = FewShotPromptTemplate(examples=examples, example_prompt=example_prompt, suffixe="问题：{input}",
    #                                input_variables=["input"]) 
    # ChatPromptTemplate.format_messages(examples)
    # print(example_prompt.format(**examples[0]))
    # print()
    # 使用语义相似性示例选择器 Chroma 开源向量数据库 OpenAIEmbeddings 数据转化成向量

    selector_from_examples = SemanticSimilarityExampleSelector.from_examples(examples, OpenAIEmbeddings(), Chroma, k=1)
    select_examples = selector_from_examples.select_examples({"question", "秦始皇和孔子谁的寿命更长"})
    for example in select_examples:
        for k, v in enumerate(example):
            print(example[k], v)
