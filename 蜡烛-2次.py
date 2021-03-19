# -*- coding: utf-8 -*-
if __name__ == '__main__':
    n = int(input())
    if n == 0: print('%.4f'% 0)
    elif n == 1: print('%.4f'% 1)
    else:
        dp = [0] * n
        res = 0

        if n & 1: # n为奇
            dp[1] = 1
            for m in range(3,n,2):
                for i in range(m//2+1,m):
                    dp[m] += 2*i
                dp[m] /= m-1

            for i in range(1,n,2):
                res += 2 * ((n-i)/2 + dp[i])
            res /= n-1
            print('%.4f'% res)
        else:
            for m in range(2,n,2):
                dp[m] += m//2
                for i in range(m//2+1,m):
                    dp[m] += 2*i
                dp[m] /= m-1

            res += n/2
            for i in range(2,n,2):
                res += 2 * ((n-i)/2 + dp[i])
            res /= n-1
            print('%.4f'% res)



