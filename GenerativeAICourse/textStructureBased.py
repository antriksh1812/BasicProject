from langchain_text_splitters import RecursiveCharacterTextSplitter

text='''A software engineer is a professional who designs, develops, tests, deploys, and maintains
software systems. They solve business and technical problems by creating reliable, efficient, and
scalable applications. Software engineers work on websites, mobile apps, enterprise platforms,
cloud systems, and AI solutions. They combine programming knowledge with analytical thinking
and collaboration to transform ideas into working software.
The software development lifecycle begins with understanding requirements. Engineers
communicate with stakeholders, designers, and product managers to identify user needs and
convert them into technical specifications. They then design system architecture, choose suitable
technologies, and implement features using languages such as Python, Java, JavaScript, C++, or
Go. Writing clean, readable, and maintainable code is a core responsibility.'''

splitter = RecursiveCharacterTextSplitter(chunk_size=40,chunk_overlap=0)
chunks = splitter.split_text(text)

for i,chunks in enumerate(chunks):
     print(i,chunks,len(chunks))