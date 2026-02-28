import json
import ollama

text = 'The sky is blue because of Rayleigh scattering'
response = ollama.embed(model='qwen3-embedding:4b', input=text)
embeddings = response.embeddings[0]

# store with metadata
with open('embedding.json', 'w') as f:
    op = {'text':text, 'embedding': embeddings}
    json.dump(op, f)
