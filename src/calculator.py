def add(a, b):
    '''
    # RUN "python -m doctest path" in terminal
    >>> add(5,7)
    12
    '''
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    '''
    # RUN "python -m doctest path" in terminal
    >>> divide(10, 0)
    Traceback (most recent call last):
    ZeroDivisionError: La division para 0 no esta definida
    '''
    if b == 0:
        raise ZeroDivisionError("La division para 0 no esta definida")
    else:
        return a / b

