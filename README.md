<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build a RAG API with FastAPI

**Project Link:** [View Project](http://nextwork.ai/projects/ai-devops-api)

**Author:** Adil  
**Email:** minhajuladil@gmail.com

---

---

## Introducing Today's Project!

In this project, I'm going to build a  RAG pipeline using FastAPI This will help me to learn how RAG system and and works. I'm interested in this because it is a project based learning system where I wont only learn about RAG or what it does but also I will gather a hands on experience on building a RAG system

### Key tools and concepts

🔍 Performed RAG (Retrieval-Augmented Generation) both manually and with code.
📄 Created a personal knowledge base using ChromaDB and vector embeddings.
🚀 Built a REST API with FastAPI that implements a full RAG pipeline.
🧠 Used nomic-embed-text for semantic search and qwen2.5:0.5b for AI response generation.
Extended the API into a multi-user AI directory with dynamic document ingestion.

### Challenges and wins

This project took me approximately 2-3 hours The most challenging part was multi tenant system

---

## Performing RAG Manually

In this step, I'm going to see RAG with a manual demo setup a Python project with a virtual environment , Install all project dependencies, and pull the nomic-embed-text embedding model to embed contexts for semantic search

![Image](http://nextwork.ai/secure_indigo_silly_rose_apple/uploads/ai-devops-api_v3j7x5b9)

### Understanding the three parts of RAG

I performed RAG manually by running ollama in my local machine.  
The three parts that I have done are:
Retrieval -> I gathered the data 
Augmented -> I added this data to my prompt 
Generation -> then I passed the whole prompt to llm to generate grounded response based on my provided data.

### Comparing the two AI models

The key difference I noticed is nomic-embed-text doesn't chat or return text like qwne2.5:0.5b, instead it returns a 768 dimensional numerical vector which mainly contains the semantic of the prompt in massive mathematical space

---

## Building a Personal Knowledge Base

In this step, I'm going to 
1. make a personal profile document 
2. Build a Python script that loads,chunks and stores my profile as embedding (converting text to numerical values in 768 dimensional vector space containing the semantic of the profile ) 
3. then I will the run the script and verify my knowledge base is built.


![Image](http://nextwork.ai/secure_indigo_silly_rose_apple/uploads/ai-devops-api_g3h7m2r5)

### Creating the profile document

I included information about myself in the text file. Now, while making the prompt ,RAG system will retrieve data about myself and will augment the prompt that will systemetically ground the LLM answer

### How semantic search finds relevant chunks

When I ask a question, ChromaDB :
1. tells embedding function to convert the query in numerical vectors, then 
2. it searchs for similar level vectors in it's database which is closest to the query.
3. the closest chunk in the db is the most similar one semantically ( meaning , context and intent) to the query



---

## Creating the RAG API with FastAPI

In this step, I'm going to build an API that will be able to receive questions , and will be able to generate answer using RAG architecture.  I'll test it using Swagger UI

![Image](http://nextwork.ai/secure_indigo_silly_rose_apple/uploads/ai-devops-api_j5m1r8t2)

### How the /ask endpoint works

When a question comes in, my endpoint
1. Retrieves the most relevant chunk from the ChromaDB 
2. Augments the prompt using relevant chunk
3. Sends the augmented prompt to LLM to generate answer

### Testing with Swagger UI

I tested my API by asking "What is Adil's goal ?". 

The AI answered with "Adil's goal is to become a full-fledged AI engineer who specializes in machine learning and deep learning applications in the production environment. He specifically aims to apply his knowledge of cloud computing, AI, and DevOps principles in implementing effective AI solutions that can be scaled up and deployed at scale for industrial or large-scale data analytics projects."

The context used was "My name is Adil.\nI'm currently learning about cloud computing, AI, and DevOps.",
    "My career goal is to become a AI engineer .\nI'm especially interested in machine learning ,deep learning usecase in production."

---

## Extending to a Multi-User AI Directory

In this project extension, I'm adding multi-user support because almost every RAG system serves multiple users. Multi-tenancy means using the same application and database to serve multiple users(tenant).Each tenant shares the same application and database, but their data and configurations are isolated and remain invisible to other tenants.

![Image](http://nextwork.ai/secure_indigo_silly_rose_apple/uploads/ai-devops-api_d5g9k3n7)

### Adding the POST /documents endpoint

In this project extension, I added a POST endpoint that receives username and content(profile) of user.Which can be used later to Retrieve information related to that specific user.  Metadata filtering allows filtering data from DB based on metadata like username , pages etc.

![Image](http://nextwork.ai/secure_indigo_silly_rose_apple/uploads/ai-devops-api_r8t2w6y1)

### Verifying multi-user filtering

In this project extension, I tested multi-user queries by providing the user metadata. The filter works because the metadata was passed to db during adding user profile to the collection.

---

## Wrapping Up

I did this project today to learn how to make a RAG system 

---

---
