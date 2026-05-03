# create a basic simple chatbot using mistral api key

from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

model = init_chat_model(model="mistral-small-2506", temperature=0.9)
message = [
    SystemMessage(content="you are a funny AI agent")
]

print("------welcome type 0 to the exit a application")
while True:
    prompt = input("you:")
    message.append(HumanMessage(content=prompt))

    if prompt == "0":
        break
    
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("Bot:", response.content)
print(message) #when we end chat so its shows chat history


