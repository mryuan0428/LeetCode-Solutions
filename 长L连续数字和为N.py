# -*- coding: utf-8 -*-
if __name__ == '__main__':
    N, L = map(int, input().split(' '))
    for l in range(L-1, 100):
        x = N/(l+1) - l/2
        if x < 0: break
        elif x == int(x): break
    
    if x < 0 or x != int(x): print('No',end='')
    else:
        for i in range(l):
            print(int(x+i), end=' ')
        print(int(x+l), end='')