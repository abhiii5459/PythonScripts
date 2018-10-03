##Illustrating the decorators concept
# Example 1
from datetime import datetime

def decorator_func(func):
    def wrapper(*args, **kwargs):
        if 7 <= datetime.now().hour < 16:
            func(*args, **kwargs)
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper