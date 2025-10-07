def require_arg_types(*types_):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) != len(types_):
                raise TypeError(
                    f"Функция {func.__name__} ожидает {len(types_)} аргументов, "
                    f"но получено {len(args)}"
                )
            for i, (arg, expected_type) in enumerate(zip(args, types_)):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Аргумент {i} функции {func.__name__} должен быть типа {expected_type.__name__}, "
                        f"но получен {type(arg).__name__}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@require_arg_types(int, str, float)
def pack(a, b, c):
    return a, b, c

print(pack(1, "x", 2.5))   
print(pack("1", "x", 2.5)) 
print(pack(1, "x"))        
