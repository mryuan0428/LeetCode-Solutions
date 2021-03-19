# -*- coding: utf-8 -*-

def bfs(grid, n):
    queue = []
    visited = set()
    # 假设0要找n-1
    for j in range(n):
        if grid[0][j] == 1:
            queue.append(j)
            visited.add(j)
    step = 1

    while queue:
        l = len(queue)
        for _ in range(l):
            p = queue.pop(0)
            if p == n-1: return step
            for j in range(n):
                if grid[p][j] == 1:
                    if j not in visited:
                        queue.append(j)
                        visited.add(j)
        step += 1
    return -1



if __name__ == '__main__':
    n, m = list(map(int, input().split(' ')))
    grid = [[0]*n for _ in range(n)]
    for i in range(m):
        a,b = map(int, input().split(' '))
        grid[a][b] = 1
    
    print(bfs(grid, n))
