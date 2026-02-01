# Goal: Create a tool that measures how long any function takes to run, without touching the function's code.
# Step 1: Create a new file in VS Code named day2_decorators.py.
# Step 2: Type this code (Do not copy-paste. Type it to feel the syntax).

import time, functools
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time

        print(f"Finished {func.__name__!r}in {run_time:4f} secs")
        return value
    return wrapper_timer
@timer
def heavy_computation(num_times):
    print(f"Calculating sum for {num_times} range")
    total = sum(range(num_times))
    return total

@timer
def sleepy_function():
    print("Sleeping for 1 second")
    time.sleep(1)
if __name__ == "__main__":
    heavy_computation(10_000_000)
    sleepy_function()