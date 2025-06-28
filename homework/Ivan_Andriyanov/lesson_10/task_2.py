def repeat_me(count=1):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return wrapper
    return actual_decorator


@repeat_me(count=2)
def example(text):
    print(text)


example("print me")
