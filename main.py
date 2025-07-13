# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
#
# #
#
#     llm = ChatOpenAI()
#     prompt = ChatPromptTemplate.from_messages(
#         [("system","你是世界技术专家"),("user","{input}")]
#
#     )
#
#     chain = prompt | llm
#
#     result=chain.invoke("input","帮我写一篇作文")
#
#     print(result)
# import os
#
# os.environ['OPENAI_API_KEY'] = 'sk-03100766b505466d8e46443af25b7e0e'