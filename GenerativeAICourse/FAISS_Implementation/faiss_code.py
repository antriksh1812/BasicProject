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

splitter = RecursiveCharacterTextSplitter(chunk_size=450,chunk_overlap=0)
chunks = splitter.split_documents(document)

#Create a vector store
embeddings = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)
results = embeddings.embed_documents([chunk.page_content for chunk in chunks])

db=FAISS.from_documents(chunks,embeddings)

query_result = "Dadasaheb Phalke Award winner"
result_select=db.similarity_search_with_score(query_result,k=2)
print(result_select)