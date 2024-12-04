# 导入所需的库
import os
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from langchain.memory import ConversationSummaryMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import TextLoader
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain

class kunkun():
    def __init__(self):
        # 在初始化方法中使用self
        self.llm = ChatOpenAI(
            api_key='sk-699af465e8174b278bf6a9df4064139e',
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            model="qwen-plus",
            # other params...
            )

        # 初始化Prompt
        self.prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    "你是一个idol，你的名字叫Kun,你喜欢唱、跳、rap、篮球，你已经练习了两年半，准备出道了，希望得到全民制作人（粉丝）的支持.你有几句口头禅，惊讶的时候会说干嘛呀，自信的时候会说厉害吧你坤哥。"
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{question}")
            ]
        )

        # 初始化Memory
        self.memory = ConversationSummaryMemory(llm=self.llm, memory_key="chat_history", return_messages=True)

        # 初始化LLMChain with LLM, prompt and memory
        self.conversation = LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            verbose=True,
            memory=self.memory
        )




    def chat_loop(self):
        print("kunkun 已启动! 输入'exit'来退出程序。")
        while True:
            user_input = input("你: ")
            if user_input.lower() == 'exit':
                print("再见!")
                break
            # 调用 llm Chain
            response = self.conversation({"question": user_input})
            print(f"kunkun: {response['text']}")
# Streamlit界面的创建
def main():
    st.title("ikun_chat")

    # Check if the 'bot' attribute exists in the session state
    if "bot" not in st.session_state:
        st.session_state.bot = kunkun()

    user_input = st.text_input("请输入你的问题：")

    if user_input:
        response = st.session_state.bot.conversation(user_input)
        st.write(f"kunkun: {response['text']}")


if __name__ == "__main__":
    main()