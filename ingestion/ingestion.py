import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

BATCH_SIZE = 200
embeddings_generator = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

def ingest_docs(document_path: str):
    
    # loader = ReadTheDocsLoader(path='/Users/vilas/Projects/ai-documentation-helper/langchain-documentation/latest')
    loader = ReadTheDocsLoader(path=document_path)
    chunks = loader.load_and_split(RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100))
    print(f"Ingesting {len(chunks)} to pincone")
    
    for i in  range(0, len(chunks), BATCH_SIZE):
        split_chunks = chunks[i : i + BATCH_SIZE]
        
        PineconeVectorStore.from_documents(documents=split_chunks, embedding=embeddings_generator, index_name=os.environ['PINECONE_INDEX_NAME'])
    
        print(f"Ingestion done until: {i + BATCH_SIZE}")
        

if __name__ == '__main__':
    print("Hello World!")
    ingest_docs()