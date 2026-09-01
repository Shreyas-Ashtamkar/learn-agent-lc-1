# from langchain.chat_models import 
from dotenv import load_dotenv
from langchain_community.llms.deepinfra import DeepInfra
load_dotenv()

model = DeepInfra(name="ibm-granite/granite-4.2-3b")

def main() -> None:
    result = model.invoke("Hello, world!")
    print(result)
