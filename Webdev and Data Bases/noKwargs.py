def no_kwargs(func):
    def wrapper(*args, **kwargs):
        if kwargs:  
            raise TypeError(f"Функция {func.__name__} не принимает именованные аргументы")
        return func(*args)
    return wrapper

@no_kwargs
def square(x):
    return x * x

print(square(4))     
print(square(x=4))   
