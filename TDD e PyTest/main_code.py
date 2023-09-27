def fun_teste(n):
    if n == 0:
        return 0
    elif n%3 == 0:
        if n%5 == 0:
            return 'Autotrac'
        return 'Auto'
    elif n%5 == 0:
        return 'Trac'
    return n
