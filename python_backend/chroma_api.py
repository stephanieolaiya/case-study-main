from fastapi import FastAPI, Request # type: ignore
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer # type: ignore
import load_docs as load_docs
import chromadb # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load embedding model
# model = SentenceTransformer("all-MiniLM-L6-v2")
model = SentenceTransformer("all-mpnet-base-v2")

# Connect to ChromaDB server
client = chromadb.HttpClient(host="localhost", port=8000)
collection = client.get_or_create_collection(name="my_collection")

# Define request model
class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_collection(request: QueryRequest):
    query_text = request.query
    embedding = model.encode([query_text])[0]
    results = collection.query(query_embeddings=[embedding], n_results=5)
    return {"results": results}
