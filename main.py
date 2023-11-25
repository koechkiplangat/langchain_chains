# This code is meant to show how the Langchain framework works
# Two large language models are chained together using SimpleSequential chain
# Single sequential chain allows for a single input and gives a single output
# The Output of the first chain is automatically taken as the input of the second chain

#importing langchain modules
from langchain.llms import OpenAI, HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

# Handling environment variables
from dotenv import load_dotenv
import os
load_dotenv()
os.environ["OPENAI_API_KEY"]
os.environ["HUGGINGFACEHUB_API_TOKEN"]

#  Defining Large Language Models to be used - OpenAI and Mistral - 7B from Hugging face
llm = OpenAI(temperature = 0.4)
llm_hug = HuggingFaceHub(repo_id= "mistralai/Mistral-7B-v0.1", model_kwargs = { "temperature" : 0.1, "max_length": 64})


country_template = PromptTemplate(
    input_variables= ["Continent"],
    template = "List the best country to visit in {Continent}. Only one country please.")

tourist_attractions_template = PromptTemplate(
    input_variables = ["Country"],
    template= "List best five historical and tourist attractions sites to visit in {Country}.Be brief."
)


chain  = LLMChain (llm=llm, prompt=country_template)

chain_hug = LLMChain(llm = llm_hug, prompt=tourist_attractions_template)

# Chaining up the above two chains 
# Setting up verbose = True gives us description of the process the LLM goes through in getting answers for querries.

chain = SimpleSequentialChain(
    chains = [chain, chain_hug],
    verbose = True)

print(chain.run("Europe"))