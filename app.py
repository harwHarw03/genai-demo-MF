# from dotenv import load_dotenv
# import os
# import streamlit as st

# from PyPDF2 import PdfReader
# # from PyPDF2.pdf import PageObject
# # from PyPDF2.generic import IndirectObject
# # from reportlab.pdfgen import canvas
# from googletrans import Translator

# from langchain.text_splitter import CharacterTextSplitter
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.chains.question_answering import load_qa_chain
# from langchain.llms import OpenAI
# from langchain.callbacks import get_openai_callback

# # def main():
# #     st.title("OTOLEGAL")
# #     st.write("Smart Legal Document Summarizer")
# #     uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# #     if uploaded_file is not None:
# #         st.write("Uploaded PDF file:", uploaded_file.name)

# #         operation = st.selectbox("Select an operation", ["Summarize PDF", "Digital Signature", "Translate PDF"])

# #         if operation == "Summarize PDF":
# #             st.subheader("Summarize PDF")
# #             print("summarize!")

# #         elif operation == "Digital Signature":
# #             st.subheader("Digital Signature")
# #             print("Signature")

# #         elif operation == "Translate PDF":
# #             st.subheader("Translate PDF")
# #             print("Trnas")

# #             translator = Translator()

# #             translated_text = ""
# #             pdf = PdfReader(uploaded_file)
# #             for page in pdf.pages:
# #                 translated_text += translator.translate(page.extract_text(), src='en', dest='your_target_language').text

# #             st.write("Translated PDF:")
# #             st.text_area("Translated Text", translated_text)


# def main():
#     load_dotenv()
#     st.set_page_config(page_title="Test LLM")
    
#     pdf = st.file_uploader("Upload your PDF", type="pdf")
    
#     # extract text
#     if pdf is not None:
#       pdf_reader = PdfReader(pdf)
#       text = ""
#       for page in pdf_reader.pages:
#         text += page.extract_text()
        
#       # split 
#       text_splitter = CharacterTextSplitter(
#         separator="\n",
#         chunk_size=1000,
#         chunk_overlap=200,
#         length_function=len
#       )
#       chunks = text_splitter.split_text(text)
      
#       embeddings = OpenAIEmbeddings()
#       knowledge_base = FAISS.from_texts(chunks, embeddings)
      
#       user_question = st.text_input("Ask a question about your PDF:")
#       if user_question:
#         docs = knowledge_base.similarity_search(user_question)
        
#         llm = OpenAI()
#         chain = load_qa_chain(llm, chain_type="stuff")
#         with get_openai_callback() as cb:
#           response = chain.run(input_documents=docs, question=user_question)
#           print(cb)
           
#         st.write(response)

# if __name__ == "__main__":
#     main()

import streamlit as st
from pages.home import app as home_app
from pages.about import app as about_app
from pages.summarize import app as summarize_app
from pages.generate import app as generate_app

apps = {
    "Home": home_app,
    "About": about_app,
    "Summarize": summarize_app,
    "Generate": generate_app
}

# st.sidebar.title("Navigation")
# selected_app = st.sidebar.radio("Select App", list(apps.keys()))
home_app()
# apps[selected_app]()

# sel = st.sidebar.radio("Select App", list(apps.keys()))
# apps[sel]()