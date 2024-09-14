from langchain.chains import LLMChain
from langchain_community.embeddings import HuggingFaceInstructEmbeddings   
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from prompt_template import memory_prompt_template
import yaml

with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

def create_llm(model_path = config["model_path"]["large"], model_type = config["model_type"], model_config = config["model_config"]):
    llm = CTransformers(model = model_path, model_type = model_type, config = model_config)
    return llm

def create_embeddings(embeddings_path = config["embeddings_path"]):
    return HuggingFaceInstructEmbeddings(embeddings_path)

def create_chain(llm, chat_prompt, memory):
    return LLMChain(llm = llm, prompt = chat_prompt, memory = memory)

def load_chain(chat_history):
    return chatChain(chat_history)

class chatChain:
    def __init__(self, chat_history):
        self.memory = ConversationBufferWindowMemory(memory_key='history', chat_memory = chat_history, k = 5)
        llm = create_llm()
        chat_prompt = PromptTemplate.from_template(memory_prompt_template)
        self.llm_chain = create_chain(llm, chat_prompt, self.memory)

    def run(self, user_input):
        return self.llm_chain.invoke(input={"human_input" : user_input, "history" : self.memory.chat_memory.messages} ,stop=["Human:"])["text"]
