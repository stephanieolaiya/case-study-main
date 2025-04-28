from sentence_transformers import SentenceTransformer
import chromadb
import json

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

with open('./webscrappers/data/fridge_cleaned_data.jsonl', 'r') as f:
    fridge_documents = [json.dumps(json.loads(line)) for line in f]

with open('./webscrappers/data/dishwasher_cleaned_data.jsonl', 'r') as f:
    dishwasher_documents = [json.dumps(json.loads(line)) for line in f] 

documents = fridge_documents + dishwasher_documents

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
