from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS


class FAISSVectorStore:

    def __init__(
        self,
        file_path: str,
        index_path: str,
        model: str = "text-embedding-3-large",
        dimensions: int = 1024,
    ):
        load_dotenv()

        self.file_path = file_path
        self.index_path = index_path

        self.embeddings = OpenAIEmbeddings(
            model=model,
            dimensions=dimensions,
        )

        self.db = None

    def load_documents(self):
        loader = TextLoader(self.file_path)
        return loader.load()

    def split_documents(
        self,
        documents,
        chunk_size=200,
        chunk_overlap=0,
    ):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )
        return splitter.split_documents(documents)

    def create_index(self):
        documents = self.load_documents()
        chunks = self.split_documents(documents)

        self.db = FAISS.from_documents(
            chunks,
            self.embeddings,
        )

        return self.db

    def save_index(self):
        if self.db is None:
            raise Exception("Index not created.")

        self.db.save_local(self.index_path)

    def load_index(self):
        self.db = FAISS.load_local(
            self.index_path,
            self.embeddings,
            allow_dangerous_deserialization=True,
        )

        return self.db

    def similarity_search(self, query, k=1):
        if self.db is None:
            raise Exception("Load or create index first.")

        return self.db.similarity_search(
            query,
            k=k,
        )

    def mmr_search(self, query, k=3):
        if self.db is None:
            raise Exception("Load or create index first.")

        retriever = self.db.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": k,
                "fetch_k": 10,
            },
        )

        return retriever.invoke(query)