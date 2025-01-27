from langchain.llms import Ollama
from langchain.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain

# loader = WebBaseLoader("https://ollama.ai/blog/run-llama2-uncensored-locally")
loader = WebBaseLoader("https://arch-as-code.org/")
docs = loader.load()

llm = Ollama(model="mistral")
chain = load_summarize_chain(llm, chain_type="stuff")

result = chain.run(docs)
print(result)