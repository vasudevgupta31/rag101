# RAG 101: Cooking Up Smart AI Answers

Think of RAG like cooking a perfect dish - you need the right ingredients and a simple recipe!

## INGREDIENTS (What You Need):

- **PDF Reader** - To read documents (like a recipe book)
- **Embedding Model** - Converts text to numbers (like a food processor)
- **Vector Database** - Stores the processed text (like a smart fridge)
- **Language Model** - Generates answers (like a master chef)

## RECIPE (Step-by-Step):

### Prep Work:
1. **Get your tools ready**
   - Install Ollama: `ollama pull qwen3-embedding:4b` and `ollama pull qwen3:4b`
   - Set up Pinecone account and get API key
   - Put your API key in `config.py`

### Cooking Steps:
2. **Chop your ingredients** - Read and chunk your PDF into bite-sized pieces
3. **Process the chunks** - Convert each text chunk into a vector (like blending)
4. **Store in the fridge** - Save all vectors in your database
5. **Take an order** - User asks a question
6. **Find the right ingredients** - Search for relevant chunks using the question
7. **Mix everything together** - Combine the question with found information
8. **Serve the dish** - Generate the final answer using the language model

## Quick Start:

```bash
# Install dependencies
poetry install

# Run individual steps
python 1_intro_to_embeddings.py
python 2_storing_embeddings.py
# ... continue through all 7 steps

# OR run the complete interactive tutorial
marimo edit rag_tutorial.py
```

## What's in the Kitchen:

- `1_intro_to_embeddings.py` - Learn about vectors
- `2_storing_embeddings.py` - How to save them
- `3_vecdb.py` - Database setup
- `4_chunking.py` - Text chopping techniques
- `5_embedding_and_storing_chunks.py` - Process and store
- `6_lm.py` - Language model basics
- `7_RAG.py` - Complete recipe in action
- `rag_tutorial.py` - Interactive cooking class
- `interstellar.pdf` - Sample document to practice with

## Perfect for:
- Learning AI fundamentals
- Building document Q&A systems
- Understanding how ChatGPT-like systems work
- Teaching RAG concepts

**Bon appétit!** Your AI system will be serving up smart answers in no time! 