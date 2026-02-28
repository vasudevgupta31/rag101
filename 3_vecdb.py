from pinecone import Pinecone,ServerlessSpec
from config import PINECONE_API_KEY

pc = Pinecone(api_key=PINECONE_API_KEY)
pc.create_index(name="rag-demo",
                dimension=2560,                    # for the embedding model we are using the dimension is 2560 (qwen3-embedding:4b)
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"))
