from backend.backend import run_llm
from ingestion.ingestion import ingest_docs
import streamlit as st

st.header("AI Documentation Helper!")

if 'chat_question_history' not in st.session_state:
    st.session_state['chat_question_history'] = []

if 'chat_answer_history' not in st.session_state:
    st.session_state['chat_answer_history'] = []


if 'document_path' not in st.session_state:
    document_path = st.text_input("Document", placeholder="Provide document path...")
    if document_path:
        st.session_state['document_path'] = document_path
        with st.spinner("Ingesting document....."):
            ingest_docs(document_path)

else:
    st.text(f"Chatting with document: {st.session_state['document_path']}")



if 'document_path' in st.session_state:
    prompt = st.text_input("Prompt", placeholder="Enter your prompt here..")

    answer = ""

    if prompt:
        with st.spinner("Generating response..."):
            response = run_llm(prompt)
            answer = response['answer']
            st.session_state['chat_question_history'].append(prompt)
            st.session_state['chat_answer_history'].append(answer)


    if 'chat_question_history' in st.session_state:
        for question, answer in zip(st.session_state['chat_question_history'], st.session_state['chat_answer_history']):
            st.chat_message("user").write(question)
            st.chat_message("ai").write(answer)