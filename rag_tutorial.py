import marimo

__generated_with = "0.20.2"
app = marimo.App(width="columns")


@app.cell(column=0)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # RAG 101: Retrieval-Augmented Generation Tutorial

    Welcome to this comprehensive tutorial on **Retrieval-Augmented Generation (RAG)**!

    In this notebook, we'll walk through building a complete RAG system from scratch, covering:

    1. **Introduction to Embeddings** - Understanding vector representations of text
    2. **Storing Embeddings** - How to persist vector data
    3. **Vector Databases** - Efficient storage and retrieval systems
    4. **Text Chunking** - Breaking documents into manageable pieces
    5. **Embedding and Storing Chunks** - Converting document chunks to vectors
    6. **Language Models** - The generation component
    7. **Complete RAG Pipeline** - Putting it all together

    ## What is RAG?

    RAG combines retrieval of relevant information with text generation to create more accurate and contextual responses. Instead of relying solely on a language model's training data, RAG retrieves relevant documents and uses them to inform the generation process.

    ## Prerequisites

    Make sure you have:
    - Ollama installed with `qwen3-embedding:4b` and `qwen3:4b` models
    - Pinecone API key (stored in config.py)
    - The required dependencies installed
    """)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 1: Introduction to Embeddings

    Embeddings are vector representations of text that capture semantic meaning. Similar texts have similar vectors in the embedding space.

    Let's start by creating our first embedding using Ollama:
    """)
    return


@app.cell
def _():
    import ollama

    # Create an embedding for a sample text
    sample_text = "The sky is blue because of Rayleigh scattering"
    response = ollama.embed(model='qwen3-embedding:4b', input=sample_text)
    embeddings = response.embeddings[0]

    print(f"Sample text: {sample_text}")
    print(f"Embedding length: {len(embeddings)}")
    return (ollama,)


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="images/emb.webp")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image("images/embspace.jpg")
    return


@app.cell
def _():
    return


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 2: Storing Embeddings

    Embeddings need to be stored efficiently for fast retrieval. We'll demonstrate basic storage concepts:
    """)
    return


@app.cell
def _(ollama):
    import json

    text = 'The sky is blue because of Rayleigh scattering'
    response_ = ollama.embed(model='qwen3-embedding:4b', input=text)
    embeddings_ = response_.embeddings[0]
    op = {'text':text, 'embedding': embeddings_}
    return (op,)


@app.cell
def _(op):
    op
    return


@app.cell
def _(mo):
    mo.image("images/vecdb.png")
    return


@app.cell
def _():
    return


@app.cell(column=3, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 3: Vector Databases

    For production systems, we need specialized vector databases that can handle:
    - Large-scale storage
    - Fast similarity search
    - Metadata filtering
    - Scalability

    We'll use Pinecone as our vector database:
    """)
    return


@app.cell
def _():
    from config import PINECONE_API_KEY
    from pinecone import Pinecone

    # Initialize Pinecone
    pc = Pinecone(api_key=PINECONE_API_KEY)

    # Connect to existing index (assuming it's already created)
    index = pc.Index('rag-demo')

    print("Connected to Pinecone vector database")
    print(f"Index name: rag-demo")

    # Get index stats
    stats = index.describe_index_stats()
    print(f"Index stats: {stats}")
    return (index,)


@app.cell
def _(mo):
    mo.image("images/vedbindex.png")
    return


@app.cell
def _():
    return


@app.cell(column=4, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 4: Text Chunking

    Large documents need to be broken into smaller chunks for effective retrieval. Different chunking strategies can impact performance:

    - **Fixed-size chunking**: Split by character count
    - **Sentence-based chunking**: Split by sentences
    - **Semantic chunking**: Split by meaning/topic
    - **Overlapping chunks**: Add overlap between chunks

    Let's implement different chunking strategies:
    """)
    return


@app.cell
def _():
    text_ = """Interstellar is a 2014 epic[5][6][7] science fiction film[1][8] directed by Christopher Nolan, who co-wrote the screenplay with his brother Jonathan Nolan. It features an ensemble cast led by Matthew McConaughey, Anne Hathaway, Jessica Chastain, Bill Irwin, Ellen Burstyn, and Michael Caine. Set in a dystopian future where Earth is suffering from catastrophic blight and famine, the film follows a group of astronauts who travel through space in search of a new home for humanity. The screenplay had its origins in a script that Jonathan had developed in 2007 and was originally set to be directed by Steven Spielberg. Theoretical physicist Kip Thorne was an executive producer and scientific consultant on the film, and wrote the tie-in book The Science of Interstellar. It was Lynda Obst's final film as producer before her death. Cinematographer Hoyte van Hoytema shot it on 35 mm film in the Panavision anamorphic format and IMAX 70 mm. Filming began in late 2013 and took place in Alberta, Klaustur, and Los Angeles. Interstellar uses extensive practical and miniature effects, and the company DNEG created additional visual effects. Interstellar premiered at the TCL Chinese Theatre on October 26, 2014, and was released in theaters in the United States on November 5, and in the United Kingdom on November 7, with Paramount Pictures distributing in the United States and Warner Bros. Pictures distributing in international markets. In the United States, it was first released on film stock, expanding to venues using digital projectors. It was a commercial success, grossing $681 million worldwide during its initial theatrical run, and $773.8 million worldwide with subsequent releases, making it the 10th-highest-grossing film of 2014. The film received generally positive reviews from critics. Among its various accolades, Interstellar was nominated for five awards at the 87th Academy Awards, winning Best Visual Effects. It also won the Hugo Award for Best Dramatic Presentation, Long Form, and the Saturn Award for Best Science Fiction Film. A sequel is in development, with Nolan set to return as director and writer."""
    return (text_,)


@app.cell
def _(text_):
    # 1. Simple chunking based on num of chars
    def chunk_text(text, chunk_size):
        return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]

    simple_chunks = chunk_text(text_, 100)


    print("Simple Chunks:")
    for i, chunk in enumerate(simple_chunks):
        print(f"Chunk {i+1}: {chunk}\n")
    return (chunk_text,)


@app.cell
def _(text_):
    # 2. Full stop based chunking (or other regex based)
    import re
    def chunk_text_regex(text, regex):
        return re.split(regex, text)

    regex_chunks = chunk_text_regex(text_, r'[.?!]')

    for i_, chunk_ in enumerate(regex_chunks):
        print(f"Chunk {i_+1}: {chunk_.strip()}\n")
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(column=5, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 5: Reading and Chunking PDF Documents

    In practice, we often work with PDF documents. Let's read a PDF and chunk it:
    """)
    return


@app.cell
def _(chunk_text):
    from pypdf import PdfReader


    def extract_text_from_pdf(pdf_path):
        reader = PdfReader(pdf_path)
        return "".join(page.extract_text() or "" for page in reader.pages)

    textpdf   = extract_text_from_pdf("interstellar.pdf")
    chunks = chunk_text(textpdf, chunk_size=500)
    return (chunks,)


@app.cell
def _(chunks):
    chunks
    return


@app.cell
def _():
    return


@app.cell(column=6, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 6: Embedding and Storing Chunks

    Now we'll convert our text chunks into embeddings and store them in our vector database:
    """)
    return


@app.cell
def _(index, ollama):
    def embed_and_store_chunks(chunks, namespace="interstellar"):
        """Embed chunks and store them in Pinecone"""
        vectors_to_upsert = []

        for i, chunk in enumerate(chunks):
            # Generate embedding
            response = ollama.embed(model='qwen3-embedding:4b', input=chunk)
            embedding = response.embeddings[0]

            # Prepare vector for upsert
            vector = {
                'id': f'chunk_{i}',
                'values': embedding,
                'metadata': {'text': chunk, 'chunk_id': i}
            }
            vectors_to_upsert.append(vector)

            # Upsert in batches of 100
            if len(vectors_to_upsert) >= 100:
                index.upsert(vectors=vectors_to_upsert, namespace=namespace)
                print(f"Uploaded batch ending at chunk {i}")
                vectors_to_upsert = []

        # Upsert remaining vectors
        if vectors_to_upsert:
            index.upsert(vectors=vectors_to_upsert, namespace=namespace)
            print(f"Uploaded final batch of {len(vectors_to_upsert)} vectors")

        print(f"Successfully stored {len(chunks)} chunks in namespace '{namespace}'")

    # # Store the first 50 chunks
    # chunks_to_store = pdf_chunks[:50]
    # print(f"Storing {len(chunks_to_store)} chunks...")
    # embed_and_store_chunks(chunks_to_store)
    return


@app.cell
def _():
    return


@app.cell(column=7, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 7: Language Models

    The generation component of RAG uses language models to produce human-like responses based on retrieved context:
    """)
    return


@app.cell
def _(ollama):
    def generate_response(prompt: str, model: str = 'qwen3:4b') -> str:
        response = ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
        return response.message.content

    test_prompt = "Explain what machine learning is in simple terms."
    test_response = generate_response(test_prompt)
    return (generate_response,)


@app.cell
def _():
    return


@app.cell(column=8, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 8: Complete RAG Pipeline

    Now let's put everything together to create a complete RAG system:
    """)
    return


@app.cell
def _(generate_response, index, ollama):
    def search_similar_chunks(query: str, top_k: int = 5, namespace: str = "interstellar"):
    
        # Generate query embedding
        query_response = ollama.embed(model='qwen3-embedding:4b', input=query)
        query_embedding = query_response.embeddings[0]

        # Search in Pinecone
        search_results = index.query(vector=query_embedding,
                                    top_k=top_k,
                                    include_metadata=True,
                                    namespace=namespace
                                )

        # Extract text and scores
        chunks_with_scores = [
            (match["metadata"]["text"], match["score"])
            for match in search_results["matches"]
        ]

        return chunks_with_scores

    def retrieve_context(query: str, top_k: int = 5) -> str:
        """Retrieve relevant context for the query"""
        chunks_with_scores = search_similar_chunks(query, top_k)

        # Combine chunks into context
        context = "\n\n".join([text for text, score in chunks_with_scores])
        return context

    def augment_prompt(query: str, context: str) -> str:
        """Create an augmented prompt with query and context"""
        prompt = f"""Answer the question using only the context below.

    Context:
    {context}

    Question: {query}

    Answer:"""
        return prompt

    def rag_pipeline(user_query: str, top_k: int = 5) -> dict:
        """Complete RAG pipeline"""
        print(f"🔍 Searching for relevant information...")

        # Step 1: Retrieve relevant context
        context = retrieve_context(user_query, top_k)

        # Step 2: Augment the prompt
        augmented_prompt = augment_prompt(user_query, context)

        print(f"📝 Generating response...")

        # Step 3: Generate response
        answer = generate_response(augmented_prompt)

        return {
            'query': user_query,
            'context': context,
            'prompt': augmented_prompt,
            'answer': answer
        }

    return (rag_pipeline,)


@app.cell
def _():
    return


@app.cell(column=9, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Interactive RAG Demo

    Let's test our RAG system with some questions about the Interstellar movie:
    """)
    return


@app.cell
def _(rag_pipeline):
    # Example questions about Interstellar
    questions = [
        "What is the name of the black hole in the movie?",
        "Who are the main characters in the movie?",
        "What is the name of the ship that the main characters are on?",
        "What is Cooper's profession?",
        "What happens to Earth in the movie?"
    ]


    question = questions[0]
    result = rag_pipeline(question)

    print("=" * 80)
    print(f"QUESTION: {question}")
    print("=" * 80)
    print(f"ANSWER: {result['answer']}")
    return


@app.cell
def _():
    return


@app.cell(column=10)
def _(mo):
    # Interactive query interface
    mo.md("### Try Your Own Query")

    # Create an interactive text input
    query_input = mo.ui.text_area(
        placeholder="Ask a question about the Interstellar movie...",
        label="Your Question:",
        full_width=True
    )

    query_input
    return (query_input,)


@app.cell
def _(mo, query_input, rag_pipeline):
    # Process the user's query if provided
    if query_input.value:
        user_result = rag_pipeline(query_input.value)

        mo.md(f"""
        **Your Question:** {user_result['query']}

        **Answer:** {user_result['answer']}

        **Retrieved Context:**
        {user_result['context'][:500]}...
        """)
    else:
        mo.md("Enter a question above to see the RAG system in action!")
    return


if __name__ == "__main__":
    app.run()
