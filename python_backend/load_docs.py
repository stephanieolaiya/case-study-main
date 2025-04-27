from sentence_transformers import SentenceTransformer
import chromadb
import json

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# # Sample documents
# documents = [
#     "Chroma is an open-source vector database.",
#     "You can use embeddings to do semantic search.",
#     "FastAPI is a Python framework for building APIs.",
#     "Vector similarity search finds related texts.",
# ]

with open('./webscrappers/data/scraped_data.jsonl', 'r') as f:
    documents = [json.dumps(json.loads(line)) for line in f]

# Generate embeddings
embeddings = model.encode(documents)

# Connect to ChromaDB server
client = chromadb.HttpClient(host="localhost", port=8000)
collection = client.get_or_create_collection(name="my_collection")

# Add documents
collection.add(
    documents=documents,
    embeddings=embeddings.tolist(),
    ids=[f"doc{i}" for i in range(len(documents))],
    metadatas=[{"source": f"doc{i}"} for i in range(len(documents))]
)

print("Documents loaded into ChromaDB.")
