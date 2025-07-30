import streamlit as st
import os
import time

# LangChain - prompt, memory, vector store, LLM
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationSummaryBufferMemory
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# Create necessary directories
os.makedirs('pdfFiles', exist_ok=True)
os.makedirs('vectorDB', exist_ok=True)

# LangChain template & memory setup
if 'template' not in st.session_state:
    st.session_state.template = """You are a knowledgeable chatbot, here to help with questions of the user. Your tone should be professional and informative.

Context: {context}
History: {history}

User: {question}
Chatbot:"""

if 'prompt' not in st.session_state:
    st.session_state.prompt = PromptTemplate(
        input_variables=["context", "history", "question"],
        template=st.session_state.template,
    )

# LLM initialization with correct model name (llama3.2)
if 'llm' not in st.session_state:
    st.session_state.llm = OllamaLLM(
        base_url='http://localhost:11434',
        model="llama3.2",
        verbose=True,
        callbacks=[StreamingStdOutCallbackHandler()]
    )

# Initialize ConversationSummaryBufferMemory with llm
if 'memory' not in st.session_state:
    st.session_state.memory = ConversationSummaryBufferMemory(
        memory_key="history",
        return_messages=True,
        input_key="question",
        llm=st.session_state.llm  # Add llm to memory initialization
    )

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Streamlit UI
st.title("Chatbot - Analyze PDFs with Local LLM")

# Show previous chat messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["message"])

# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    st.text("File has been uploaded without any issues")

    file_path = os.path.join("pdfFiles", uploaded_file.name)

    if not os.path.exists(file_path):
        with st.status("Saving file..."):
            with open(file_path, 'wb') as f:
                f.write(uploaded_file.read())

            # Load and split PDF
            loader = PyPDFLoader(file_path)
            data = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            all_splits = text_splitter.split_documents(data)

            # Create vectorstore using correct model
            st.session_state.vectorstore = Chroma.from_documents(
                documents=all_splits,
                embedding=OllamaEmbeddings(model="llama3.2")
            )

            # Initialize retriever
            st.session_state.retriever = st.session_state.vectorstore.as_retriever()

    # Initialize the QA chain
    if 'qa_chain' not in st.session_state:
        st.session_state.qa_chain = RetrievalQA.from_chain_type(
            llm=st.session_state.llm,
            chain_type='stuff',
            retriever=st.session_state.retriever,
            verbose=True,
            chain_type_kwargs={
                "verbose": True,
                "prompt": st.session_state.prompt,
                "memory": st.session_state.memory,
            }
        )

    # Chat input logic
    if user_input := st.chat_input("You:", key="user_input"):
        # Show user message
        user_message = {"role": "user", "message": user_input}
        st.session_state.chat_history.append(user_message)
        with st.chat_message("user"):
            st.markdown(user_input)

        # Get assistant response
        with st.chat_message("assistant"):
            with st.spinner("Assistant is typing..."):
                response = st.session_state.qa_chain(user_input)
            full_response = ""
            message_placeholder = st.empty()
            for chunk in response['result'].split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + " ")
            message_placeholder.markdown(full_response)

        chatbot_message = {"role": "assistant", "message": response['result']}
        st.session_state.chat_history.append(chatbot_message)
