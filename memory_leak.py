# Vulnerable: Unbounded global collection accumulation leading to Memory Leak (CWE-400)
GLOBAL_REQUEST_CACHE = []

def record_telemetry(data: dict):
    # Appends continuously without LRU eviction, time-to-live, or maximum size
    GLOBAL_REQUEST_CACHE.append(data)
    return len(GLOBAL_REQUEST_CACHE)
