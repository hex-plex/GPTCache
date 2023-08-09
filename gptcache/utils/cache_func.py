def cache_all(*_, **__):
    return True

def cache_control(*args, **kwargs):
    to_cache_enable = kwargs.get("ingestion", True)
    return to_cache_enable