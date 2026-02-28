# 🍳 RAG 101: Cooking Up Smart AI Answers

Think of RAG like cooking a perfect dish - you need the right ingredients and a simple recipe!

## 🥘 INGREDIENTS (What You Need):

- **PDF Reader** 📖 - To read documents (like a recipe book)
- **Embedding Model** 🧠 - Converts text to numbers (like a food processor)
- **Vector Database** 🗄️ - Stores the processed text (like a smart fridge)
- **Language Model** 🤖 - Generates answers (like a master chef)

## 👨‍🍳 RECIPE (Step-by-Step):

### Prep Work:
1. **Get your tools ready** 🔧
   - Install python (if you dont have)
   - Install Ollama from `https://ollama.com/download`
   - Download required models: `ollama pull qwen3-embedding:4b` and `ollama pull qwen3:4b`
   - Set up Pinecone account and get API key (`https://www.pinecone.io/`)
   - clone this repository in a folder by either download this with the code (green) button or using the command `git clone https://github.com/vasudevgupta31/rag101.git
   - CD into this folder
   - Create a file called config.py and write this line PINECONE_API_KEY=<your_api_key>
   - Install poetry with: pip install poetry
   - run `poetry install` (this will install python libraries used to run the code)
   - run `python 3_vecdb.py` (this will create an index in your pinecone to be used to store vectors)

### Cooking Steps:
2. **Chop your ingredients** ✂️ - Read and chunk your PDF into bite-sized pieces  (Run `python 5_embedding_and_storing_chunks.py`) This will do this step and the next #3, #4 and #5 also. If you want you can change the pdf file that you want to try. Make sure that file is available in the folder itself.
3. **Process the chunks** 🥄 - Convert each text chunk into a vector (like blending) (Already done if you've done #2)
4. **Store in the fridge** ❄️ - Save all vectors in your database                 (Already done if you've done #2)
5. **Take an order** 📝 - User asks a question                                    (Run `python 7_RAG.py` -> change your question inside this for LM to fetch stuff from your vecdb and your pdf) This generates the answer also
6. **Find the right ingredients** 🔍 - Search for relevant chunks using the question
7. **Mix everything together** 🥗 - Combine the question with found information   
8. **Serve the dish** 🍽️ - Generate the final answer using the language model

## 🚀 Quick Start:

```bash
# Run individual steps
python 3_vecdb.py
python 5_embedding_and_storing_chunks.py
python 7_RAG.py
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
- Teaching RAG concepts

**Bon appétit!**
