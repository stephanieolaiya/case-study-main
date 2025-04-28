## Python Backend

This contains code to: 
1. Run the webscrapper to scrape parts from PartSelect website: 
    ```
    cd webscrappers
    python parts_scrape.py
    ```
    To add more product types, run for product_url of the given type e.g 
    https://www.partselect.com/Refrigerator-Parts.htm. 
    ScraperAPI key is needed to run webscrapper script. Create .env file
    based on .env.example provided. 

    Data files are in the webscrappers/data folder in jsonl format. 

2. Load documents into ChromaDB vector database and start Microservice API 
to query database based on user query from frontend.

### To get python backend started
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
