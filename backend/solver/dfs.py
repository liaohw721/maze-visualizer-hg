from solver.common import exist


def solveDFS(grid, start, end):
    path = []
    steps = []
    row = len(grid)
    col = len(grid[0])
    visited = [[False] * col for i in range(row)]
    color = grid
    if not exist(start[0], start[1], row, col) or not exist(end[0], end[1], row, col):
        x = {"steps": [], "path": [], "status": "invalid input"}
        return x

    def dfs(x, y):
        visited[x][y] = True
        steps.append({"x": x, "y": y, "color": "green"})
        path.append([x, y])
        if end == (x, y):
            return True
        for i in (-1, 0), (0, 1), (1, 0), (0, -1):
            if exist(x + i[0], y + i[1], row, col):
                steps.append({"x": x + i[0], "y": y + i[1], "color": "bold"})
            else:
                continue
            if not grid[x + i[0]][y + i[1]] and not visited[x + i[0]][y + i[1]]:
                steps.append({"x": x, "y": y, "color": "red"})
                if dfs(x + i[0], y + i[1]):
                    return True
                steps.append({"x": x, "y": y, "color": "green"})
        steps.append({"x": x, "y": y, "color": "white"})
        return False

    if dfs(start[0], start[1]):
        x = {"steps": steps, "path": path, "status": "success"}
    else:
        x = {"steps": steps, "path": path, "status": "no path"}
    return x
