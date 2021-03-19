# -*- coding: utf-8 -*-
MAX_value = float('inf')

def dijkstra(graph, s):
    # 判断图是否为空，如果为空直接退出
    if graph is None:
        return None
    
    # 最终结果
    dist = graph[0].copy()
    dist[s] = 0

    S = [s]
    Q = [i for i in range(1,len(graph))]

    while Q:
        #更新距离
        for i in range(len(graph)):
            if graph[s][i] + dist[s] < dist[i]:
                dist[i] = graph[s][i] + dist[s]
        
        #找最小
        minimun = float('inf')
        
        #有到达不了的：
        s = -1
        for v in Q:
            if minimun > dist[v]:
                minimun = dist[v]
                s = v
        if s != -1:
            S.append(s)
            Q.remove(s)
        else: break
        
    return dist


if __name__ == '__main__':
    # n个节点，m条边
    n, m = list(map(int, input().split(' ')))
    graph = [[MAX_value] * n for _ in range(n)]

    for i in range(m): 
        s, e = list(map(int, input().split(' ')))
        graph[s][e], graph[e][s] = 2 ** i, 2 ** i
    
    dist = dijkstra(graph, 0)
    for i in range(1,n):
        if dist[i] == MAX_value:
            print(-1)
        else:
            print(dist[i]%100000)











