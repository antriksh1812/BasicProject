from dotenv import load_dotenv;
from langchain_openai import OpenAIEmbeddings
load_dotenv()      #loading the environmental files


query =["Hello","My name is Antriskh","How you doing","I work for Kpn"]

embeddings = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)
results = embeddings.embed_documents(query)
print(results)
print(len(results[0]))

