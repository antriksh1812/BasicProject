from langchain_community.retrievers import WikipediaRetriever

query ="Who is Hrithik Roshan"
retriever = WikipediaRetriever(top_k_results=1,lang='en')
ans = retriever.invoke(query);
for i,docs in enumerate(ans):
    print(i,docs)