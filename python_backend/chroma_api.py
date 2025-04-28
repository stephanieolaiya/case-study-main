from fastapi import FastAPI, Request
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import load_docs as load_docs
import chromadb
from fastapi.middleware.cors import CORSMiddleware


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
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB server
client = chromadb.HttpClient(host="localhost", port=8000)
collection = client.get_or_create_collection(name="my_collection")

# add metadata filtering for fridge and dishwasher
# def extract_metadata(query):
#     query = query.lower()
#     metadata = {}

#     if "dishwasher" in query:
#         metadata["category"] = "dishwasher"
#     elif "fridge" in query or "refrigerator" in query:
#         metadata["category"] = "refrigerator"

#     known_brands = ["whirlpool", "lg", "samsung", "ge", "bosch"]
#     for brand in known_brands:
#         if brand in query:
#             metadata["brand"] = brand
#             break

#     return metadata

# Define request model
class QueryRequest(BaseModel):
    query: str


@app.post("/query")
async def query_collection(request: QueryRequest):
    query_text = request.query

    # Generate embedding
    embedding = model.encode([query_text])[0]

    # Query ChromaDB
    results = collection.query(query_embeddings=[embedding], n_results=3)

    return {"results": results}
