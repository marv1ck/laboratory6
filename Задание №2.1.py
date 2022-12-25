graph = {'1': ['2', '5'],
         '2': ['1', '3', '6', '7'],
         '3': ['2', '4', '8'],
         '4': ['3', '8'],
         '5': ['1', '7'],
         '6': ['2'],
         '7': ['2', '5', '8'],
         '8': ['3', '4', '7', '9'],
         '9': ['8']}
from collections import deque
def shirina(start, end, graph):
    queue = deque([start])
    visited = {start: None}
    while queue:
        a = queue.popleft()
        if a == end:
            break
        b = graph[a]
        for c in b:
            if c not in visited:
                queue.append(c)
                visited[c] = a
    return visited
start = '1'
end = '9'
visited = shirina(start, end, graph)
a = end
print(f'Путь от {end} до {start}: {end} ', end='')
while a != start:
    a = visited[a]
    print(f'-> {a} ', end='')