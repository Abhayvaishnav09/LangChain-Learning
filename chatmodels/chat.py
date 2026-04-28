from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

# model = init_chat_model("mistral-small")
# model = init_chat_model("llama3-8b-8192", model_provider="groq")
# We use llama-3.1-8b-instant as it has the most generous free-tier limits.
# max_tokens restricts the maximum number of tokens it can generate in the response.
model = init_chat_model("groq:llama-3.1-8b-instant", max_tokens=50)
response = model.invoke("give me an paragraph on ai")

print(response.content)


# concept of temperature  0 to 1:  if you want creative response like write poem so we use 1 high temperature AND if we want mathematician or logical task so use 0 .