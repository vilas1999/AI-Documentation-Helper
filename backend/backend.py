import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_pinecone import PineconeVectorStore


from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain


load_dotenv()

def run_llm(query: str):
    embeddings_generator = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    vector_store = PineconeVectorStore(embedding=embeddings_generator, index_name=os.environ['PINECONE_INDEX_NAME'])
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

    retrieval_qa_prompt = hub.pull("langchain-ai/retrieval-qa-chat", include_model=True)
    combine_chain_docs = create_stuff_documents_chain(llm, retrieval_qa_prompt)
    chain = create_retrieval_chain(vector_store.as_retriever(), combine_chain_docs)

    return chain.invoke(input={"input": query})

