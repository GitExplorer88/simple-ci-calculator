def total(x, y):
    return x + y


def difference(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by Zero")
    return x / y
