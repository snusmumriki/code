def get_value(weight, n, p):
    value = [[]]
    for i in range(weight):
        value[0][i] = 0
    for i in range(n):
        value[i][0] = 0  # Первые элементы приравниваем к 0
    for k in range(1, n):
        for s in range(1, weight):  # Перебираем для каждого k все вместимости
            if s >= weight[k]:  # Если текущий предмет вмещается в рюкзак
                value[k][s] = max(value[k - 1][s], value[k - 1][s - weight[k]] + p[k])  # Выбираем класть его или нет
            else:
                value[k][s] = value[k - 1][s]  # Иначе, не кладем


def find_ans(k, s, value, weight):
    ans = []
    while value[k][s] != 0:
        if value[k - 1][s] == value[k][s]:
            k -= 1
        else:
            k -= 1
            s -= weight[k]
            ans.append(k)
    return ans
