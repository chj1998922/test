def log_decrator(level):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if level == "INFO":
                print("INFO")
                func()
                print("**")
            else:
                print("ELSE")
                func()
                print("wan")
        return wrapper
    return decorator

@log_decrator("INF")
def say_hello():
    print("hello")


say_hello()