from functools import wraps

def limit(limit: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if wrapper.call_count >= limit:
                raise RuntimeError(
                    f"Function '{func.__name__}' can only be called {limit} times.")
            wrapper.call_count += 1
            return func(*args, **kwargs)

        wrapper.call_count = 0
        return wrapper
    return decorator
