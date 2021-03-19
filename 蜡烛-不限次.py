# -*- coding: utf-8 -*-
if __name__ == '__main__':
    n = int(input())
    if n == 0: print(0)
    if n == 1: print(1)
    dp = [0] * (n+1)
    
    if n & 1: # n为奇
        dp[1] = 1 
        for x in range(3,n+1,2):
            for y in range(1,x,2):
                dp[x] += 2 * ((x-y)/2 + dp[y])
            dp[x] /= x-1
        print(dp[n])
    
    else:
        dp[0] = 0
        for x in range(2,n+1,2):
            dp[x] +=  x/2 + dp[0]
            for y in range(2,x,2):
                dp[x] += 2 * ((x-y)/2 + dp[y])
            dp[x] /= x-1
        print(dp[n])


