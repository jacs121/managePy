from functools import wraps

def retry(tries: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(tries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == tries - 1:
                        raise e.add_note("retry: ran out of tries")
        return wrapper
    return decorator
