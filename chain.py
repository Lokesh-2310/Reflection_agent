from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

load_dotenv()

llm=ChatOpenAI(model="o4-mini-2025-04-16")

generate_prompt=ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are the helful assistant for students who provide explanation of topic."
         "If the user provides critique, respond with a revised version of your previous attempts."
         "If revised version is generated do not mention any heading like revised version etc."
         ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)


revisor_prompt=ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are best tutor for students.!Mandatory Generate ~3-5 critique and recommendations for the below answer like for emojis in text if needed, examples, mathematical formula etc wherever needed."),
        MessagesPlaceholder(variable_name="messages")
    ]
)

generate_chain=generate_prompt | llm
revisor_chain=revisor_prompt | llm



