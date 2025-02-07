from app.core.config import cache

def get_cached_response(cache_key):
    cached_response = cache.get(cache_key)
    if cached_response:
        return eval(cached_response)
    return None

def cache_response(cache_key, response, expiration=3600):
    cache.set(cache_key, str(response), ex=expiration)