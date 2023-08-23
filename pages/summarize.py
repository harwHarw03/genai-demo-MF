import streamlit as st
from utils.pdf import read_pdf
from utils.summarizer import summarize
import os
from langchain.llms import CerebriumAI 
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from PyPDF2 import PdfReader

def app():
    st.image("logo.png", width=100)
    st.title("Summarizer Page")
    st.write("Upload a PDF or input text below to summarize legal documents.")
    
    uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"])

    # if uploaded_file is not None:
    #     pdf_reader = read_pdf(uploaded_file)
    #     text = ""
    #     for page in pdf_reader.pages:
    #         text += page.extract_text()

    #     text_splitter = CharacterTextSplitter(
    #         separator="\n",
    #         chunk_size=1000,
    #         chunk_overlap=200,
    #         length_function=len
    #     )
    #     chunks = text_splitter.split_text(text)     
        # extract text
    texted = ""
    if uploaded_file is not None:
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
      # split 
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        # st.write(text)    
        texted = text

    os.environ["CEREBRIUMAI_API_KEY"] = "public-d2fa255c0ef40a9482f4"

    llm = CerebriumAI(
      endpoint_url="https://run.cerebrium.ai/gpt4-all-webhook/predict",
      max_length=100
    )
    chain = load_qa_chain(llm, chain_type="stuff")
    
    # response = chain.run(input_documents=docs, question=user_question)
    # test = "summarize : My name is Rudy, and I am a recent electronics bachelor's graduate with a deep fascination for the realm of quantum computing. I am writing to express my keen interest in the pioneering research conducted at your esteemed lab in the field of quantum computing. Your lab's exceptional work, particularly in areas like [mention a specific project or achievement], has captured my attention and motivated me to explore potential opportunities for involvement. The prospect of contributing to your lab's groundbreaking endeavors is truly exciting to me. I am intrigued by the collaborative and innovative environment that your lab provides, and I am eager to contribute my skills and enthusiasm to this dynamic research space. I would greatly appreciate the chance to learn more about your ongoing projects and discuss how my background in electronics could align with your research goals. Thank you for considering my inquiry, and I look forward to the possibility of contributing to the transformative work being conducted at MIT"
    test = "paraphrase this but just write the pharaphrased: his name is rudy and he want to join the to professor john lab about quantum computer"
    # test += texted
    st.write(llm(test))


    #     file_contents = uploaded_file.read()
    #     st.write("Text from PDF:")
    #     st.write(file_contents)
        
        # if st.button("Summarize"):
        #     text = read_pdf(file_contents) 
        #     summary = summarize(text)  
        #     st.write("Summary:")
        #     st.write(summary)

app()