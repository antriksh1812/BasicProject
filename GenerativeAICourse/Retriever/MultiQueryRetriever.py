from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers import MultiQueryRetriever
from dotenv import load_dotenv
import logging


load_dotenv()  
llm = ChatOpenAI(model='gpt-3.5-turbo',temperature=0)
embeddings = OpenAIEmbeddings()
docs =[
        'Eat Fruit to imporove gut health',
        'Excercise more and do stregth training',
        'Increase your fiber intake',
        'Dhoni is a great finisher',
        'Modi ji is  prime minister of india'
      ]
vector_store = FAISS.from_texts(docs,embeddings)
mqr = MultiQueryRetriever.from_llm(retriever=vector_store.as_retriever(),llm=llm)
result = mqr.invoke('How can I  stay fit')

print('Multi Query Results')
for i,result in enumerate(result):
    print(result)




