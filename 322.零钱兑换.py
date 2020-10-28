#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (41.33%)
# Likes:    882
# Dislikes: 0
# Total Accepted:    146.8K
# Total Submissions: 351.9K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 
# 你可以认为每种硬币的数量是无限的。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1
# 
# 示例 2：
# 
# 
# 输入：coins = [2], amount = 3
# 输出：-1
# 
# 示例 3：
# 
# 
# 输入：coins = [1], amount = 0
# 输出：0
# 
# 
# 示例 4：
# 
# 
# 输入：coins = [1], amount = 1
# 输出：1
# 
# 
# 示例 5：
# 
# 
# 输入：coins = [1], amount = 2
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: 
            return 0
        
        coins_s = [i for i in coins if i <= amount]
        
        l = len(coins_s)
        if l == 1 and coins_s[0] == 1: 
            return amount
        if l < 1:
            return -1
        
        for i in range(l):
            if coins_s[i] == amount:
                return 1
        
        dp = [10001]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            p=[]
            for c in coins_s:
                p.append(dp[i-c]+1 if i>=c else 10001)
            dp[i] = min(p)
        if dp[amount] > 10000:
            return -1
        else:
            return dp[amount]

# @lc code=end

