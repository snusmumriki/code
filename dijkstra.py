def search(graph, start, end):
    tracks = [None] * len(graph)
    tracks[start] = [start]  # уровень начальной вершины
    stack = [start]  # добавляем начальную вершину в очередь
    while stack:  # пока там что-то есть
        node = stack.pop()  # извлекаем вершину
        for i in graph[node]:  # запускаем обход из вершины node
            if tracks[i] is None:  # проверка на посещенность
                stack.append(i)  # добавление вершины в очередь
                tracks[i] = tracks[node] + [i]  # подсчитываем уровень вершины
    return tracks[end]
