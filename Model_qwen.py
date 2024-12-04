#导入相关包
import os


from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
os.environ["DASHSCOPE_API_KEY"]='sk-699af465e8174b278bf6a9df4064139e'
from langchain_community.llms import Tongyi
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


llm = Tongyi(temperature=1)
template = '''
        你的名字是小黑子,当人问问题的时候,你都会在开头加上'唱,跳,rap,篮球!',然后再回答{question}
    '''
prompt = PromptTemplate(
    template=template,
    input_variables=["question"]  # 这个question就是用户输入的内容,这行代码不可缺少
)
chain = LLMChain(  # 将llm与prompt联系起来
    llm=llm,
    prompt=prompt
)
question = '你是谁'

res = chain.invoke(question)  # 运行

print(res['text'])  # 打印结果
