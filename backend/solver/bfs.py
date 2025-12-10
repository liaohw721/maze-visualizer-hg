from solver.common import exist
from collections import deque

def solveBFS(grid, start, end):
    path = []
    steps = []
    row = len(grid)
    col = len(grid[0])
    visited = [[False] * col for i in range(row)]
    color = grid
    if not exist(start[0], start[1], row, col) or not exist(end[0], end[1], row, col):
        x = {"steps": [], "path": [], "status": "invalid input"}
        return x
    queue = deque()
    queue.append(start)

    while queue:
        a, b = queue.popleft()
        if not visited[a][b]:
            visited[a][b] = True
            steps.append({"x": a, "y": b, "color": "green"})
            path.append([a, b])
            if end == (a, b):
                c = {"steps": steps, "path": path, "status": "success"}
                return c
            for i in (-1, 0), (0, 1), (1, 0), (0, -1):
                if exist(a + i[0], b + i[1], row, col):
                    steps.append({"x": a + i[0], "y": b + i[1], "color": "bold"})
                else:
                    continue
                if not grid[a + i[0]][b + i[1]] and not visited[a + i[0]][b + i[1]]:
                    queue.append([a+i[0],b+i[1]])
                    steps.append({"x": a+i[0], "y": b+i[1], "color": "lightskyblue"})

            steps.append({"x": a, "y": b, "color": "red"})

    c = {"steps": steps, "path": path, "status": "no path"}
    return c
                 

