import numpy as np
from transformers import pipeline

# Load the model
model_name = "sentence-transformers/all-MiniLM-L6-v2"
nlp_transformers = pipeline("feature-extraction", model=model_name)

def create_embeddings(descriptions):
    return np.array([np.mean(nlp_transformers(desc), axis=1).squeeze() for desc in descriptions])

def create_query_embedding(query):
    return np.mean(nlp_transformers(query), axis=1).squeeze()