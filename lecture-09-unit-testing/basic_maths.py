def add(first, second):
    return first + second


def multiply(first, second):
    return first * second


def division(first, second):
    if second == 0:
        raise ValueError("Second param is zero")
    return first / second
