from ollama import chat, embed
from config import PINECONE_API_KEY
from pinecone import Pinecone

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index('rag-demo')

def search(query: str, top_k: int = 20):
    q_vec = embed(model='qwen3-embedding:4b', input=query).embeddings[0]
    results = index.query(vector=q_vec, top_k=top_k, include_metadata=True, namespace='interstellar')
    return [(m["metadata"]["text"], m["score"]) for m in results["matches"]]


def retreive(query: str, top_k: int = 20):
    chunks = search(query, top_k)
    return "\n\n".join([text for text, score in chunks])


def augment(query: str, context):
    prompt =  f"""Answer the question using only the context below.
Context:
{context}
Question: {query}
"""
    return prompt


def generate(prompt):
    response = chat(model='qwen3:4b', messages=[{'role': 'user', 'content': prompt}])
    return response.message.content



# RAG
user_query = "What is the name of the ship that the main characters are on in the movie Interstellar?"
# user_query = "Who are the main characters in the movie?"
# user_query = "What is the name of the black hole in the movie?"
context = retreive(user_query)
prompt = augment(user_query, context)
answer = generate(prompt)

print("Question:", user_query)
print("Answer  :", answer)
