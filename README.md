------------------------------------------------------------
                        RAG 101                     
------------------------------------------------------------

## INGREDIENTS:

# 0. Pdf reader
# 1. Embedding Model 
# 2. Vector DB
# 3. LM


## Recipe:

# 1. Download a pdf reader in your programming language
# 2. Select an embedding model (we will use ollama, we can also use an api - most famous is openai) (Every model has a specific vector len)
# 3. Read and chunk the pdf text with a fixed lengh
# 4. Convert each chunk into its respective vector 
# 5. Store the vectors in a vector DB (we will use redis right now but there are many options like pinecone, qdrant, weaviate etc)
# 6. Let user ask a query
# 7. Lets generate embedding of the query and find the most relevant peices from our vector store
# 8. Give the user query and the relevant pieces found to an LLM
# 9. LM generates answer for the user



# ollama helpers:
# (https://ollama.com/download)
# ollama pull qwen3-embedding:4b
# 