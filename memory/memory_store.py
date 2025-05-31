import redis
import json
from datetime import datetime

r = redis.Redis(host='localhost', port=6379, db=0)

def log_to_memory(thread_id: str, data: dict):
    data['timestamp'] = datetime.utcnow().isoformat()
    r.set(thread_id, json.dumps(data))

def get_from_memory(thread_id: str):
    raw = r.get(thread_id)
    if raw:
        return json.loads(raw)
    return {}
