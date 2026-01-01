def cache_results(func):
    # Write your code below this line
    cache = {}
    def wrapper(*args):
        if args in cache:
            return f"From Cache: {cache[args]}"
        result = func(*args)
        cache[args] = result
        return f"Computed: {result}"
    return wrapper


@cache_results
def multiply(a: int, b: int) -> int:
    return a * b

multiply(5, 5)
multiply(5, 2)
multiply(5, 5)