#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (50.96%)
# Likes:    1365
# Dislikes: 0
# Total Accepted:    328.4K
# Total Submissions: 644.3K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 注意：给定 n 是一个正整数。
# 
# 示例 1：
# 
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 
# 示例 2：
# 
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# 
# 
#
# 数学： 
''' n
全1: 1
1个2: n-1 选 1
2个2: n-2 选 2
k个2: n-k 选 k
直到 n-k < k

或者：通项公式
f(n) = f(n-1)+f(n-2) 
# 1动态规划   「滚动数组思想」把空间复杂度优化成 O(1)
# 2差分方程
'''
# @lc code=start
class Solution:
    def method1(self, n):
        p = 0
        q = 0
        r = 1

        for i in range(n):
            p = q
            q = r
            r = p + q
        return r

    def method2(self, n):
        # 差分方程(n)=f(n−1)+f(n−2)，特征方程：x^2 = x + 1
        # 特征根：x_1，x_2 = \frac{1-\sqrt{5}}{2}x 
        # f(n) = c_1 * x_1 ^n + c_2 * x_2 ^ n，代入初始条件f(1)=1，f(2)=1，得 c_1，c_2
        sqrt5 = 5 ** 0.5
        fibn = (((1 + sqrt5)/2) ** (n+1)) - (((1 - sqrt5)/2) ** (n+1))
        return int(fibn/sqrt5)




    def climbStairs(self, n: int) -> int:
        return self.method2(n)
# @lc code=end

