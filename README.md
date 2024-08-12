this tool has a lot of decorator and functions for managing or restricting other functions for unique purpose

such as:

1. **limit**

   ```python
   from managePy.limit import limit

   # insert how many times the function is allowed to run
   @limit(limit=3)
   def my_function():
       print("Function called!")

   my_function()  # run once
   my_function()  # run twice
   my_function()  # run three times
   my_function()  # This will raise an exception and will not run the function
   ```
2. **retry**

```python
from managePy.retry import retry

# insert how many times managePy should try to run the function the function
@retry(tries=5)
def unreliable_function():
    import random
    if random.choice([True, False]):
        raise ValueError("Random failure")
    return "Success"

print(unreliable_function()) # if retry failed it will add the line "retry: ran out of tries" to the exception
```

3. **selfDestruct**

```python
from managePy.selfDestruct import selfDestruct
from managePy.init import Inits

# insert the amount of seconds until the function can not be used anymore
@selfDestruct(timeout=5)
def my_function():
    print("Executing my_function.")

init_manager = Inits()

# Activate the self-destruct for my_function
init_manager.activateDestruct(my_function)

my_function()  # Should work
threading.Event().wait(2)
my_function()  # Should work
threading.Event().wait(5)
my_function()  # Should raise an exception (function destroyed)
```
