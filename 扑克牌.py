# -*- coding: utf-8 -*-
def solution(n, m, k): # 动态规划 -- 子问题dp[i][j]从i副牌选j！！！
    if k < n or k > n * m: return 0
    elif k == n or k == n*m: return 1
    else:
        dp = [[0] * k for _ in range(n)]
        for i in range(1, k):
            dp[1][i] = 1
            dp[i][i] = 1
        for i in range(2, n):
            for j in range(i+1, k):
                







        res = 0
        if k-n+1 > m:
            l = m
        else: l = k-n+1
        for i in range(1, l+1):
            res += solution(n-1, m, k-i)
        return res

if __name__ == '__main__':
    T = int(input())
    ans = []
    for _ in range(T):
        n, m, k = map(int, input().split(' '))
        ans.append(solution(n, m, k))
    for i in ans:
        print(i%(1e9+7))
