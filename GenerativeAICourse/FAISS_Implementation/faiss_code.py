from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()      #loading the environmental files


#load the documement

loader = TextLoader('/Users/antrikshtyagi/Workspace/Projects/BasicProject/GenerativeAICourse/ChromaDbCode/bestheroes.txt')
document = loader.load()
#print(document[0].page_content)

#Do the text splitting

splitter = RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=0)
chunks = splitter.split_documents(document)

#Create a vector store
embeddings = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=1024)


db=FAISS.from_documents(chunks,embeddings)
db.save_local("/Users/antrikshtyagi/Workspace/Projects/BasicProject/GenerativeAICourse/FAISS-Implementation/FAISS_Indexing")
db_new = db.load_local('/Users/antrikshtyagi/Workspace/Projects/BasicProject/GenerativeAICourse/FAISS-Implementation/FAISS_Indexing',embeddings,allow_dangerous_deserialization=True)

#print(type(db))
query_result = "who is called as King of Bollywood"
result_select=db_new.similarity_search(query_result,k=1)
print(result_select)



