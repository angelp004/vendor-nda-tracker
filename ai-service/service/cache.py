import redis
import hashlib

# Redis connection
r = redis.Redis(host='localhost', port=6379, db=0)

# Generate cache key
def get_cache_key(input_text):
    return hashlib.sha256(input_text.encode()).hexdigest()