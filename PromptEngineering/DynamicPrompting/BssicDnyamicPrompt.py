from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()



context="Indian culture is one of the oldest and richest cultures in the world." \
" It is known for its great diversity, traditions, customs, festivals, languages, f" \
"ood, clothing, music, dance, art, and literature. India is home to people belonging to " \
"different religions and communities, yet they live together with a spirit of unity " \
"and harmony. Festivals such as Diwali, Holi, Eid, Christmas, Pongal, Baisakhi, " \
"and Durga Puja are celebrated with great enthusiasm and bring people together." \
" Respect for parents, elders, teachers, and guests is an important part of " \
"Indian culture, and the saying “Atithi Devo Bhava” means that guests should be " \
"treated like gods. Indian food is also an important part of its culture, with different " \
"regions having their own special dishes and cooking styles. " \
"Traditional clothes such as sarees, salwar suits, kurtas, " \
"and dhotis reflect the cultural diversity of the country. " \
"India is also famous for classical dances like Bharatanatyam, Kathak, Kathakali, and " \
"Odissi, as well as its rich traditions of yoga and meditation. Indian culture teaches " \
"values such as kindness, respect, peace, cooperation, and family unity. " \
"Although India is developing rapidly and adopting modern lifestyles, " \
"it continues to preserve its ancient traditions and values. " \
"This beautiful combination of old traditions and modern ideas makes " \
"Indian culture unique and admired throughout the world."

prompt_teplate= PromptTemplate(template="You are a smart assistant. You need to use the " \
"context {context} to answer the question {question}. If you dont know the answer then simply " \
"say . I cant help you")

fnlPrompt = prompt_teplate.invoke({'context':context,'question':'What are the famous dances'})

llm = ChatOpenAI(model='gpt-3.5-turbo',temperature=0.2)
result = llm.invoke(fnlPrompt)
print(result.content)