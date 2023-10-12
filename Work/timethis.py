import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start =  time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__module__:s}.{func.__name__:s}: {end-start:f}")
        return r
    return wrapper
