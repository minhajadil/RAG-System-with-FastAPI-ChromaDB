import chromadb
from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)




#makes a db 
client =  chromadb.PersistentClient(path='./chroma_db')

# the function that converts the text into embedding 
ef = OllamaEmbeddingFunction(
    model_name='nomic-embed-text',
)

# a seperate collection of data in DB , embedded by the ef function
collection = client.get_or_create_collection(
    name = "personal_profile",
    embedding_function= ef
)









with open("profile.txt","r") as file:
    text = file.read()



chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

print(f"loaded {len(chunks)} chunks from profile")

# storing in chromadb 



# adding data to collection 
collection.add(
    ids = [f"chunk{i}" for i in range(len(chunks))], # unique IDs for each chunk of the data
    documents = chunks,
    metadatas = [{"source":"profile","chunk_index":i} for i in range(len(chunks))]
)



print(f"Added {len(chunks)} chunks to the 'personal_profile' collection.")
print("Knowledge base built successfully!")
