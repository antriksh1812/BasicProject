from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader('GenerativeAICourse/software_engineer_introduction_500_words.pdf')
documents = loader.load()
print(f"length of documents {len(documents)}")
splitter = CharacterTextSplitter(chunk_size=300,chunk_overlap=30,separator='') # we got the spliter object now
chunks = splitter.split_documents(documents);
print(chunks[0].page_content)

'''text="My name is Antriksh and I am a software developer . I work in Techmahindra and I am working as a software enginner." \
"I want to achieve a good life . I love my daughter very much"

splitter = CharacterTextSplitter(chunk_size=30,chunk_overlap=5,separator='')
chunks =splitter.split_text(text)

for i,chunks in enumerate(chunks):
    print(i,chunks)'''
