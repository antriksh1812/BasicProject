from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

reviewStr ='''The iPhone 17 is a premium smartphone that combines a stylish design, 
powerful performance, an impressive camera system, and a smooth user experience. 
Its bright and responsive display makes watching videos, browsing, and gaming enjoyable, 
while its powerful processor handles multitasking and demanding apps efficiently. 
The iPhone 17 also offers a high-quality camera for capturing detailed photos and videos, a
long with the secure and user-friendly iOS operating system. Its five main advantages are its 
premium design, fast performance, excellent camera quality, smooth display, 
and secure software experience. However, it also has some disadvantages, 
including its high price, limited customization compared with Android phones, 
expensive accessories, some charging and connectivity limitations, and the higher 
cost of larger storage options. Overall, the iPhone 17 is a great choice for users who want a 
premium, reliable, and powerful smartphone, although its price may be a major 
consideration.
'''

class Review(BaseModel):
    Product : str =Field(description="Name of the product mentioned in description",default="None")
    ProductCons : list[str]=Field(description="All the negative features of the product")
    ProdPros:list[str]=Field(description="All the positive features of the product")


llm = ChatOpenAI(model='gpt-3.5-turbo',temperature=0.2)

structure = llm.with_structured_output(Review)
result = structure.invoke(reviewStr)

print(result.json())