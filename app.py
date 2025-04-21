from flask import Flask, render_template, request
from src.helper import download_hugging_face_embeddings
from langchain_community.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain_community.llms import CTransformers
from dotenv import load_dotenv
from src.prompt import prompt
import os
import pinecone

app = Flask(__name__)
load_dotenv()

# Load Pinecone API credentials
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')
index_name = "medhelp"

# Initialize embedding model
embeddings = download_hugging_face_embeddings()

# Initialize Pinecone
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(index_name)
docsearch = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)

# Load LLM
llm = CTransformers(
    model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config={"max_new_tokens": 512, "temperature": 0.7}
)

# Setup the QA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=docsearch.as_retriever(search_kwargs={"k": 2}),
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt},
    return_source_documents=True
)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    user_msg = request.form["msg"]
    print("\n🧑‍💬 User:", user_msg)

    result = qa({"query": user_msg})

    # 🔍 Print retrieved context chunks
    print("\n📚 Retrieved Context Chunks:")
    for i, doc in enumerate(result["source_documents"], 1):
        print(f"\nChunk {i}:\n{doc.page_content}\n{'-' * 60}")

    # 🤖 Print bot's response
    print("\n🤖 Bot:", result["result"])

    return result["result"]

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
