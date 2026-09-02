# from langchain.chat_models import 
from dotenv import load_dotenv
from langchain_community.llms.deepinfra import DeepInfra

load_dotenv()

model = DeepInfra(name="openai/gpt-oss-20b", model_kwargs={
    "system_prompt": "Be a helpful assistant, that translates English to French.",
    "max_new_tokens" : 64,
    "temperature": 0.3,
    "top_p": 0.9,
    "min_p": 0.3,
    "top_k": 7,
    "repetition_penalty": 2,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "service_tier": "default",
})

def main() -> None:
    conv = [
        # { "role": "system",    "content": "You are a helpful assistant that translates English to French." },
        { "role": "user",      "content": "Translate: I love programming." },
        { "role": "assistant", "content": "J'adore la programmation." },
        { "role": "user",      "content": "Translate: I love agents" },
    ]
    result = model.invoke(conv)
    print(result)
