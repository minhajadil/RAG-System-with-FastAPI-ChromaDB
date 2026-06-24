from fastapi import FastAPI
import ollama
import chromadb
from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)
from pydantic import BaseModel # Validates incoming request data







app = FastAPI()






#makes a db 
client =  chromadb.PersistentClient(path='./chroma_db')

# the function that converts the text into embedding 
ef = OllamaEmbeddingFunction(
    model_name='nomic-embed-text',
    url="http://localhost:11434",
)

# a seperate collection of data in DB , embedded by the ef function
collection = client.get_or_create_collection(
    name = "personal_profile",
    embedding_function= ef
)







#define the expected shape for post
class DocumentSubmission(BaseModel):
    user_name : str 
    content : str  


@app.post("/documents") #POST endpoint
def add_document(submission: DocumentSubmission):

    # Split into chunks by paragraph - each blank line becomes a split point
    # strip() removes extra whitespace, and the if-check skips empty chunks
    chunks = [chunk.strip() for chunk in submission.content.split("\n\n") if chunk.strip()]

    # adding data to collection 
    collection.add(
    ids = [f"{submission.user_name}-chunk{i}" for i in range(len(chunks))], # unique IDs for each chunk of the data
    documents = chunks,
    metadatas = [{"source":"profile", "user_name" : submission.user_name, "chunk_index":i} for i in range(len(chunks))]
    )

    return {
        "message": f"Added {len(chunks)} chunks for user '{submission.user_name}'.",
        "user_name": submission.user_name,
        "chunks_added": len(chunks),
    }












@app.get("/ask")
def ask(question : str, user : str =None):


    query_params ={

        "query_texts": [ question ], # ChromaDB converts this into a vector and searches for similar chunks
        "n_results" : 2,
    }

    if user:
        query_params["where"] = {"username": user} # where in metadata
    





    # Step 1 : RETRIEVE - Seach ChromaDB for 2 most relevant chunks
    relevant = collection.query(**query_params)

    context = "\n\n".join(relevant['documents'][0])

    # Step 2: AUGMENT - build a prompt that includes the retrieved context
    
    augmented_prompt = f"""Use the following context to answer the question.
                     If the context doesn't contain relevant information, say so.

                    Context:
                        {context}

                    Question: {question}"""
    response = ollama.chat(
        model ='qwen2.5:0.5b',
        messages=[{"role": "user" , "content" :augmented_prompt }],
    )

    return {
        "question" : question,
        "answer" : response["message"]["content"],
        "context_used" : relevant["documents"][0],
        "filtered_by_user" : user
    }
    






@app.get("/debug/db")
def debug_database(user: str = None):
    # This fetches the raw text and metadata directly, bypassing the AI models
    if user:
        return collection.get(where={"user_name": user})
    return collection.get()