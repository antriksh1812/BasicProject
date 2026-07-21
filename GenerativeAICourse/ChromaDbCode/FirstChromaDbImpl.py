from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
load_dotenv()      #loading the environmental files


#load the documement

loder = TextLoader('bestheroes.txt')
document = loder.load();
print(document)