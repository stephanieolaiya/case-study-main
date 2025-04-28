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


## NB: 
- Not in DB: 
Could not extract related link: /Refrigerator-Hardware.htm
Could not extract related link: /Refrigerator-Switches.htm
Could not extract related link: /Refrigerator-Electronics.htm
Could not extract related link: /Refrigerator-Dispensers.htm
Could not extract related link: /Refrigerator-Timers.htm
Could not extract related link: /Refrigerator-Springs-and-Shock-Absorbers.htm
Could not extract related link: /Refrigerator-Ducts-and-Vents.htm

Could not extract related link: /Blomberg-Dishwasher-Parts.htm
Could not extract related link: /Kelvinator-Dishwasher-Parts.htm
Could not extract related link: /LG-Dishwasher-Parts.htm