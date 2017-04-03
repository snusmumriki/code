class Monster:
    def __init__(self, time, health):
        self.time = time
        self.health = health


class Word:
    def __init__(self, damage, rate):
        self.damage = damage
        self.rate = rate


def tf(arg):
    return (arg + j) % 1000001


def tfw(w):
    w.damage, w.rate = tf(w.damage), tf(w.rate)
    return w


n, mana = map(int, input().split())
d = []
words = []
res = []
j = 0
for i in range(n):
    k, a, b = map(int, input().split())
    if k == 1:
        words.append(Word(a, b))
    else:
        word = max(map(tfw, words), key=lambda w: w.damage / w.rate)
        monster = Monster(tf(a), tf(b))
        d.append(word)
        d.append(word)
        is_win = monster.health / word.damage < mana / word.rate
        res.append(is_win)
        if is_win:
            j = i

for is_win in res:
    print('YES' if is_win else 'NO')
