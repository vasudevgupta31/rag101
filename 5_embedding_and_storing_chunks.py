import ollama
from tqdm import tqdm
from pypdf import PdfReader
from pinecone import Pinecone
from config import PINECONE_API_KEY

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    return "".join(page.extract_text() or "" for page in reader.pages)

def chunk_text(text, chunk_size=1000):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

text   = extract_text_from_pdf("interstellar.pdf")
chunks = chunk_text(text, chunk_size=500)

pc    = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("rag-demo")
namespace = "interstellar"

batch = []
for i, chunk in enumerate(tqdm(chunks, desc="Embedding")):
    embedding = ollama.embed(model='qwen3-embedding:4b', input=chunk).embeddings[0]
    batch.append({"id": str(i), "values": embedding, "metadata": {"text": chunk}})

for i in range(0, len(batch), 100):
    index.upsert(vectors=batch[i:i+100], namespace=namespace)

