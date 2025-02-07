from fastapi import FastAPI
from app.api.v1.search import router as search_router
from app.services.faiss_service import load_data_into_faiss

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    load_data_into_faiss()

app.include_router(search_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)