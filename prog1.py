def func1(x, y):
    return x and not y


row = [0, 1, 1, 0]
print(list(map(func1, row + [0], [0] + row))[:-1])
