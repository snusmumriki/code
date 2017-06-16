n, s = map(int, input().split())
res = 0
if s >= n:
    print(0)
else:
    for n in range(n, 1, -1):
        res += n - sum(map(int, str(n))) >= s
    print(res)
