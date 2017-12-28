def func(x1, x2, y1, a, b, y2):
    if x <= x1:
        return y1
    elif x1 < x <= x2:
        return a * x + b
    else:
        return y2


f = [None] * int(input())
l, r, x = map(int, input().split())
#for