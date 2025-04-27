## To get python backend started
1. Start chroma db server: 
```
chroma run --host 0.0.0.0 --port 8000
```

2. Load documents into chroma
```
python load_docs.py
```

3. Start FastAPI server (that frontend connects to):
```
uvicorn chroma_api:app --host 0.0.0.0 --port 8001 --reload
```