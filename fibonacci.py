def fibonacci(n):
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
