class Monster:
    def __init__(self, time, health):
        self.time = time
        self.health = health


class Word:
    def __init__(self, damage, rate):
        self.damage = damage
        self.rate = rate


n, mana = map(int, input().split())
word = None
res = []
j = 0
for i in range(n):
    k, a, b = map(int, input().split())
    a = (a + j) % 1000001
    b = (b + j) % 1000001
    if k == 1:
        word = max((word, Word(a, b)), lambda w: w.damage / w.rate)
    else:
        is_win = Monster(a, b).health / word.damage < mana / word.rate
        j += is_win
        res.append(is_win)

for is_win in res:
    print('YES' if is_win else 'NO')
