from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')  # Optional now

# Step 1: Load and process the documents
extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

# Step 2: Initialize Pinecone client (v3+)
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medhelp"

# Step 3: Create index if it doesn't exist
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  # Adjust based on your embedding model (e.g., MiniLM is 384)
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-west-2"  # Or your actual Pinecone region
        )
    )

# Step 4: Connect to existing index
index = pc.Index(index_name)

# Step 5: Store embeddings using LangChain wrapper
docsearch = LangchainPinecone.from_texts(
    [t.page_content for t in text_chunks],
    embeddings,
    index_name=index_name,
    namespace="medhelp-namespace"  # Optional: helps avoid collisions
)
