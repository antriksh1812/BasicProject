from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()      #loading the environmental files


#load the documement

loder = TextLoader('/Users/antrikshtyagi/Workspace/Projects/BasicProject/GenerativeAICourse/ChromaDbCode/bestheroes.txt')
document = loder.load();
#print(document[0].page_content)

#Do the text splitting

splitter = RecursiveCharacterTextSplitter(chunk_size=450,chunk_overlap=0)
chunks = splitter.split_documents(document)


#Create a vector store

vector_store = Chroma(embedding_function=OpenAIEmbeddings(),persist_directory="/Users/antrikshtyagi/Workspace/Projects/BasicProject/GenerativeAICourse/ChromaDbCode/ChromaDatabase",collection_name="first_collection")
add_result =vector_store.add_documents(chunks)

query ="Who is Salman Khan"
ret =vector_store.as_retriever(search_kwargs={"k":1})
answer = ret.invoke(query)
print(answer)