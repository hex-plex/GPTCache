def cache_all(*_, **__):
    return True

def cache_control(*args, **kwargs):
    to_cache_enable = kwargs.get("ingestion", False)
    return to_cache_enable