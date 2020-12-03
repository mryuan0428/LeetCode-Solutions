#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (36.68%)
# Likes:    543
# Dislikes: 0
# Total Accepted:    104.4K
# Total Submissions: 280K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# 
# 
# 示例 2：
# 
# 输入：n = 0
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：n = 1
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 5 * 10^6
# 
# 
#
# 思路1: 埃式筛法 O(nloglogn)
# 思路2: 欧式筛法 O(n)
# @lc code=start
class Solution:
    def Es(self, n):
        isPrime = [1] * n
        res = 0

        for i in range(2,n):
            if isPrime[i]:
                res += 1
                j = i 
                while j * i <= n-1:
                    isPrime[j*i] = 0
                    j += 1
        return res


    def Os(self, n):
        isPrime = [1] * n
        Primes = []

        for i in range(2,n):
            if isPrime[i]:
                Primes.append(i)
            for j in Primes:
                t = i * j
                if t < n:
                    isPrime[t] = 0
                    if i % j == 0:
                        break
                else:break
        return len(Primes)

    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        else: return self.Os(n)

# @lc code=end

