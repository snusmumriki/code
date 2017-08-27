from functools import reduce
from itertools import chain, groupby
from operator import and_


def func(r, x):
    k, v = x
    return r + (k and len(list(v)) == 1)


def func1(x, y):
    return x and not y


n, m = map(int, input().split())
storage = [list(map(lambda x: x == '.', input())) for _ in range(0, n)]
zstorage = list(map(list, zip(*storage)))
cstorage = list(chain(*storage))

i = sum(cstorage)  # всего пустых мест
j = reduce(func, groupby(cstorage), 0) + 1  # одиноких пустых мест

storage = [list(map(func1, row + [False], [False] + row))[:-1] for row in storage]
zstorage = [list(map(func1, column + [False], [False] + column))[:-1] for column in zstorage]
zstorage = list(zip(*zstorage))

i -= sum(map(and_, chain(*storage), chain(*zstorage)))
res = 2 ** i * j
print(res % 1000000007)
