from functools import reduce


def bfs(user_, adj):
    a, b = user_
    tracks = [None] * len(adj)
    tracks[a] = [a]
    stack = [a]
    while stack:
        node = stack.pop()
        for i in adj[node]:
            if tracks[i] is None:
                stack.append(i)
                tracks[i] = tracks[node] + [i]
    return tracks[b]


def func(tmp):
    users = [set(bfs(user, city)) for user in tmp]
    inc = []
    using = [0] * (n - 1)
    for user in users:
        inc.append([])
        i = 0
        for admin in admins:
            if admin.issubset(user):
                inc[-1].append(i)
                using[i] += 1
            i += 1
    print(using)
    u = 1
    res_u = set()
    res_a = set()
    for admin in inc:
        for a in admin:
            if using[a] <= 1:
                res_u.add(u)
            else:
                res_a.add(a + 1)
        u += 1
    return res_u, res_a


n, m = map(int, input().split())
city = [[] for _ in range(n)]
admins = []
for _ in range(n - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    city[x].append(y)
    city[y].append(x)
    admins.append({x, y})
users_ = [tuple(map(lambda p: int(p) - 1, input().split())) for _ in range(m)]

res_user, res_admin = func(users_)
length = len(set(users_))
length1 = len(res_user) + len(res_admin)
if length < length1:
    length1 = length
    res_user = range(1, m + 1)
    res_admin = ()

print(length1)
print(len(res_user), *res_user)
print(len(res_admin), *res_admin)
