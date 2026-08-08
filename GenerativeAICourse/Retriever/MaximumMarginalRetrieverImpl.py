from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv();

embeddings = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=1024);

#AlternateApproach  Text--->TextL

docs =[
         'India is a multicultural country and having multiple states',
         'Each State has their own culture',
         'Delhi is capital of india',
         'Narendara Modi is PM of india'
      ]

store = FAISS.from_texts(docs,embeddings)

query ="Give details about India"

retriever = store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 3,           # Number of documents returned
        "fetch_k": 10,    # Number of candidate documents to consider
        "lambda_mult": 0  # Balance between relevance and diversity
    }
)

result =retriever.invoke(query)
for i,result in enumerate(result):
    print(result.page_content)
    print("----------")