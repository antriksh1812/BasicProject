from langchain_community.retrievers import WikipediaRetriever

query ="Who is Hrithik Roshan"
retriever = WikipediaRetriever(k=3,lang='en')
ans = retriever.invoke(query);
for i,docs in enumerate(ans):
    print(i,docs) 