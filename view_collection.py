import chromadb
from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)
import json

# Connect to the database
client = chromadb.PersistentClient(path='./chroma_db')

# the function that converts the text into embedding 
ef = OllamaEmbeddingFunction(
    model_name='nomic-embed-text',
    url="http://localhost:11434",
)

# Get the collection
collection = client.get_or_create_collection(
    name="personal_profile",
    embedding_function=ef
)

# Get all data from collection
all_data = collection.get()

print("=" * 80)
print("COLLECTION DATA")
print("=" * 80)
print(f"\nTotal documents: {len(all_data['documents'])}\n")

# Print each document with its metadata
for i, (doc_id, document, metadata) in enumerate(zip(all_data['ids'], all_data['documents'], all_data['metadatas'])):
    print(f"--- Document {i+1} ---")
    print(f"ID: {doc_id}")
    print(f"Metadata: {json.dumps(metadata, indent=2)}")
    print(f"Content:\n{document}")
    print()

print("=" * 80)
