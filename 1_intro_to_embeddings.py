import ollama

response = ollama.embed(model='qwen3-embedding:4b', input='The sky is blue because of Rayleigh scattering')
embeddings = response.embeddings[0]


print("-"*50)
print("Embedding values:", embeddings)
print("-"*50)
print("Embedding length:", len(embeddings))
print("-"*50)