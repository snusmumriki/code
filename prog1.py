class Monster:
    def __init__(self, time, health):
        self.time = time
        self.health = health


class Word:
    def __init__(self, damage, rate):
        self.damage = damage
        self.rate = rate


def func():
    while mana:
        pass
    j += True


n, mana = map(int, input().split())
words = []
monsters = []
j = 0
for _ in range(n):
    k, a, b = map(int, input().split())
    a = (a + j) % 1000001
    b = (b + j) % 1000001
    if k == 1:
        words.append(Word(a, b))
    else:
        monsters.append(Monster(a, b))
