# Langchain Framework Example

This code demonstrates the chaining aspect of the Langchain framework. It showcases how two large language models can be seamlessly connected using SimpleSequentialChain. In this example, a single sequential chain is created, allowing for a single input that generates a single output. The output of the first chain is automatically passed as the input to the second chain.

## Features
- Utilizes Langchain modules for language model management.
- Incorporates two large language models: OpenAI and Mistral-7B from Hugging Face.
- Environment variables are handled using the `dotenv` library for enhanced security.
- Defines prompt templates for querying information about the best country to visit in a given continent and the top historical and tourist attractions in a specified country.
- Demonstrates the chaining of the two language models for a cohesive response.
- The `SimpleSequentialChain` is employed to connect the OpenAI and Hugging Face models.

The given instance involves seeking recommendations for the ideal European destination and subsequently detailing the prime historical and tourist attractions in the chosen country. 
The selection of the country is conducted by the OpenAI LLM, while the Mistral-7B LLM is employed for listing historical sites in the country given by the first chain - the OpenAI LLM.


## Instructions
1. Ensure you have the necessary API keys set up for OpenAI and Hugging Face Hub by setting the corresponding environment variables.
2. Run the code and observe the chained behavior of the two language models.

