from langchain_community.document_loaders import TextLoader

loader = TextLoader("MyFile.txt")
documents = loader.load()
print(len(documents))
