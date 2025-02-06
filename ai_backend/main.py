from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import mysql.connector
import faiss
import numpy as np

app = FastAPI()

# Load the model
model_name = "sentence-transformers/all-MiniLM-L6-v2"
nlp = pipeline("feature-extraction", model=model_name)

# Database connection
db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'academic_system'
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# FAISS index
index = faiss.IndexFlatL2(384)  # Dimension of embeddings

class Query(BaseModel):
    query: str

def load_menu_data():
    cursor.execute("SELECT id, description, alias, department FROM menus")
    rows = cursor.fetchall()
    descriptions = [row[1] for row in rows]
    embeddings = np.array([np.mean(nlp(desc), axis=1).squeeze() for desc in descriptions])
    index.add(embeddings)
    return rows

rows = load_menu_data()

@app.post("/search_menu")
async def search_menu(query: Query):
    query_embedding = np.mean(nlp(query.query), axis=1).squeeze()
    D, I = index.search(np.array([query_embedding]), k=1)
    result = rows[I[0][0]]
    return {
        "id": result[0],
        "description": result[1],
        "alias": result[2],
        "department": result[3]
    }

@app.post("/extract_entities")
async def extract_entities(query: Query):
    # Example extraction logic (to be replaced with actual implementation)
    entities = {
        "menu": "Regular Semester Mark Card",
        "batch": "BCOMA",
        "batch_start_year": "2022",
        "semester": "6th Semester"
    }
    return entities

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)