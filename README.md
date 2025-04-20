# AI Documentation Helper

## Table of Contents
1. [Introduction](#introduction)
2. [Key Features](#key-features)
3. [Architecture](#architecture)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Example](#example)
8. [Roadmap](#roadmap)
9. [Acknowledgements](#acknowledgements)

---

## Introduction
A AI assistant that enables interactive chat-based Q&A with your documents.

## Key Features
- **Flexible Input**: Supports individual files or entire directories of documents.
- **Powered by LangChain**: Modular orchestration for pipelines.
- **Google AI Models**: Embeddings and LLM via GoogleAI APIs.
- **Pinecone Vector DB**: High-performance similarity search for embeddings.

## Architecture
### Components
- **LangChain**: Manages document ingestion, embedding, and query chains.
- **Google AI**: Provides embedding vectors and language model completions.
- **Pinecone**: Stores embeddings and handles similarity search.

### Data Flow
1. **Document Ingestion**: Read and preprocess documents from specified path.  
2. **Embedding Generation**: Convert text chunks into vectors via Google AI.  
3. **Indexing**: Push vectors into Pinecone for retrieval.  
4. **Chat Interface**: User queries trigger vector search and LLM response generation.

## Installation
TBA

## Configuration
1. Copy `.env.example` to `.env`.  
2. Set the following in `.env`:  
   - `GOOGLE_API_KEY`  
   - `PINECONE_API_KEY`  
   - `PINECONE_ENV`  

## Usage
TBA

## Example
```text
> python main.py --doc-path ./docs
Loading 5 documents...  
Generating embeddings...  
Indexed 500 vectors.  

You: What is the main purpose of the API?
AI: The API allows clients to perform CRUD operations on user resources...
```

## Roadmap
- [ ] Support additional file formats (e.g., PPTX, DOCX)  
- [ ] Add multi model support
- [ ] Add local vector database support

## Acknowledgements
- [LangChain](https://github.com/langchain/langchain)  
- [Pinecone](https://www.pinecone.io/)  
- [Google AI](https://cloud.google.com/ai)
