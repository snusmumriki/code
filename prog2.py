nums = set()
res = []
for j in range(0, int(input())):
    com = tuple(map(int, input().split()))
    tmp = set(range(com[1], com[2] + 1))
    if com[0] == 1:
        nums |= tmp
    elif com[0] == 2:
        nums -= tmp
    else:
        nums ^= tmp
    if nums:
        for i in range(1, max(nums) + 2):
            if i not in nums:
                res.append(i)
                break
    else:
        res.append(1)

for r in res:
    print(r)
