from functools import wraps

def selfDestruct(timeout, forceQuit: bool = False):
    """add a timer that will 'destroy' the function after a specified timeout.
    This will prohibit the function from being called."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Start the timer on the first call
            if not wrapper.timer_started:
                wrapper.timer.start()
                wrapper.timer_started = True
            if wrapper.destroyed:
                if forceQuit:
                    raise RuntimeError(
                        f"Function '{func.__name__}' has been destroyed and cannot be called.")
                print(f"Function '{
                      func.__name__}' has been destroyed and cannot be called.")
            else:
                return func(*args, **kwargs)

        def self_destruct():
            wrapper.destroyed = True

        # Initialize the wrapper attributes
        wrapper.destroyed = False
        wrapper.timer_started = False
        wrapper.self_destruct = self_destruct
        return wrapper
    return decorator
