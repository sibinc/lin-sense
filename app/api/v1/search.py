from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from app.services.faiss_service import search_faiss_index
from app.services.cache_service import get_cached_response, cache_response
from app.services.nlp_service import create_query_embedding

router = APIRouter()

class SearchQuery(BaseModel):
    query: str

@router.post("/search")
async def search(query: SearchQuery, background_tasks: BackgroundTasks):
    response = {}
    query_embedding = create_query_embedding(query.query)

    # Check the cache first
    cache_key = f"search:{query.query}"
    cached_response = get_cached_response(cache_key)
    if cached_response:
        return cached_response

    # Menu search
    menu_result = search_faiss_index(query_embedding, index_type="menu")
    if menu_result:
        response['menu'] = menu_result

    # Entity extraction
    entity_results = search_faiss_index(query_embedding, index_type="entity")
    if entity_results:
        response['entities'] = entity_results

    if not response:
        raise HTTPException(status_code=404, detail="No results found")

    # Cache the response
    cache_response(cache_key, response)

    return response