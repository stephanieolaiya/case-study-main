from sentence_transformers import SentenceTransformer # type: ignore
import chromadb # type: ignore
import json

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create documents from data files
documents = []

data_files_path = ['./webscrappers/data/fridge_cleaned_data.jsonl', 
                   './webscrappers/data/dishwasher_cleaned_data.jsonl',
                   './webscrappers/data/dishwasher_repair.jsonl',
                    './webscrappers/data/fridge_repair.jsonl'
                   ]

for file_path in data_files_path:
    with open(file_path, 'r') as f:
        file_content = [json.dumps(json.loads(line)) for line in f]
        documents += file_content

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
