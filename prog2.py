n = int(input())
coms = [tuple(map(int, input().split())) for _ in range(0, n)]
nums = set()
for com in coms:
    tmp = set(range(com[1], com[2] + 1))
    if com[0] == 1:
        nums |= tmp
    elif com[0] == 2:
        nums -= tmp
    else:
        nums ^= tmp
    tmp = set(range(1, max(tmp) + 2)) - nums
    print(min(tmp))
