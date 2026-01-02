import os
import chainlit as cl
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Configuration
PDF_FOLDER = "pdfs"  # Folder containing PDF files
CHROMA_DB_DIR = "chroma_db"  # Directory for vector database


def load_and_process_pdfs():
    """Load PDFs from folder and create vector store"""
    
    # Check if PDF folder exists
    if not os.path.exists(PDF_FOLDER):
        os.makedirs(PDF_FOLDER)
        return None, "PDF folder created. Please add PDF files to the 'pdfs' folder and restart the app."
    
    # Check if there are any PDF files
    pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith('.pdf')]
    if not pdf_files:
        return None, "No PDF files found in the 'pdfs' folder. Please add some PDF files and restart the app."
    
    # Load PDFs
    try:
        loader = PyPDFDirectoryLoader(PDF_FOLDER)
        documents = loader.load()
    except Exception as e:
        return None, f"Error loading PDF files: {str(e)}. Please ensure PDFs are valid and not password-protected."
    
    if not documents:
        return None, "Could not load any text from PDF files. They may be empty, corrupted, or contain only images."
    
    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_documents(documents)
    
    # Create embeddings and vector store
    embedding_model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-ada-002")
    embeddings = OpenAIEmbeddings(model=embedding_model)
    
    # Create or load vector store
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR
    )
    
    return vectorstore, f"Successfully loaded {len(pdf_files)} PDF file(s) with {len(chunks)} chunks."


@cl.on_chat_start
async def start():
    """Initialize the chat session"""
    
    # Send welcome message
    await cl.Message(
        content="🤖 Welcome to PDF Chat App! Loading your PDF files..."
    ).send()
    
    # Load and process PDFs
    vectorstore, status_message = load_and_process_pdfs()
    
    # Send status message
    await cl.Message(content=status_message).send()
    
    if vectorstore is None:
        return
    
    # Create conversation chain
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )
    
    # Get model name from environment or use default
    model_name = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    
    llm = ChatOpenAI(
        model=model_name,
        temperature=0
    )
    
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        memory=memory,
        return_source_documents=True,
        verbose=False
    )
    
    # Store chain in user session
    cl.user_session.set("chain", chain)
    
    await cl.Message(
        content="✅ Ready! Ask me anything about your PDF documents."
    ).send()


@cl.on_message
async def main(message: cl.Message):
    """Handle incoming messages"""
    
    # Get the chain from user session
    chain = cl.user_session.get("chain")
    
    if chain is None:
        await cl.Message(
            content="❌ Chat chain not initialized. Please restart the app."
        ).send()
        return
    
    # Send a thinking message
    msg = cl.Message(content="")
    await msg.send()
    
    # Get response from chain
    response = await cl.make_async(chain.invoke)({"question": message.content})
    
    answer = response["answer"]
    source_documents = response.get("source_documents", [])
    
    # Format response with sources
    if source_documents:
        sources = set()
        for doc in source_documents:
            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", "N/A")
            # PyPDF uses 0-based page numbering, so we add 1 for display
            page_display = page + 1 if isinstance(page, int) else page
            sources.add(f"{os.path.basename(source)} (Page {page_display})")
        
        sources_text = "\n\n📚 **Sources:**\n" + "\n".join(f"- {s}" for s in sources)
        answer = answer + sources_text
    
    # Update message with response
    msg.content = answer
    await msg.update()


if __name__ == "__main__":
    # This is handled by Chainlit CLI
    pass
