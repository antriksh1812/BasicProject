from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()
#getTheTranscript
def getTranscriptObj(videoId):
     if not videoId:
          return None

     try:
          yt_obj = YouTubeTranscriptApi()
          return yt_obj.fetch(videoId)
     except Exception as ex:
          print(ex)
          return None
     else:
          print("Step01:Transcipt Created Sucessfully")


# create chunks
 
def getChunkedData(documentText):
     if not documentText:
          return None;
     try:
          splitterObj = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
          data        = splitterObj.split_text(documentText)
          return data;
     except Exception as ex:
           print(ex)
           return None
     else:
          print("Step02: Chunking is successful")

#Define Embedding Function

def getEmbeddingObj(modelVersion):
     if not modelVersion:
          return None
     print("Step03:Embedding Model Created")
     return OpenAIEmbeddings(model=modelVersion,dimensions=1024);

#Save to Vector Store
def insertVectorStore(embedding,chunks):
     if not embedding and not chunks:
          return None;
        
     try:
          db=FAISS.from_texts(chunks,embedding)
          
     except Exception as ex:
          print(ex)
          return None
     else:
          print("Step 04:Vector Store Created Successfully")
          return db;

#PromptTemplate

def createPromptTemplate(templateStr,variableList):
      if not templateStr and not  variableList and len(variableList)==0:
           return None;
      try:
           promptTemplate = PromptTemplate(template=templateStr,input_variables=variableList)
           return promptTemplate;
      except Exception as ex:
           print(ex)
           return None
      else:
           print("Step05 : Template Created Successfully")

############# Begin Invoking
videoId ="o126p1QN_RI"
transcript = getTranscriptObj(videoId)
formatted_text = "".join(doc.text for doc in transcript)

chunks = getChunkedData(formatted_text)

embeding = getEmbeddingObj('text-embedding-3-large');

db = insertVectorStore(embeding,chunks)
retriever = db.as_retriever(seach_kwargs={'k':4})
query="What is juice"
context = retriever.invoke(query)
intial_template ='''You are helpful assistance .Answer from the folloing context
 if the context is insufficient or irrelevant then say I dont know {context} question {question}'''
prompt = createPromptTemplate(intial_template,['context','question'])
#print(f"Heyy the value of prompt is {prompt}")
fimal_prompt = prompt.invoke({'question':query,'context':context})
llm = ChatOpenAI(model='gpt-3.5-turbo',temperature=0.2)
result = llm.invoke(fimal_prompt)
print(result.content)