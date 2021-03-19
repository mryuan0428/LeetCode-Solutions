# -*- coding: utf-8 -*-
if __name__ == '__main__':
    r, c = list(map(int, input().split(' ')))
    res = []
    for i in range(r):
        res.append(list(input().split(' ')))
    
    new_res = [[] for _ in range(c)]
    
    for j in range(c):
        for i in range(r):
            new_res[j].append(res[i][j])
    for j in range(c):
        print(' '.join(new_res[j]))

