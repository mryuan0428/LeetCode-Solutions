#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#
# https://leetcode-cn.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (54.78%)
# Likes:    525
# Dislikes: 0
# Total Accepted:    87.4K
# Total Submissions: 159.5K
# Testcase Example:  '[0,0,0,0]'
#
# 数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
# 
# 每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。
# 
# 请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：cost = [10, 15, 20]
# 输出：15
# 解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
# 
# 
# 示例 2：
# 
# 
# 输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出：6
# 解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。
# 
# 
# 
# 
# 提示：
# 
# 
# cost 的长度范围是 [2, 1000]。
# cost[i] 将会是一个整型数据，范围为 [0, 999] 。
# 
# 
#
# 动态规划：dp[n] = min(dp[n-1]+cost[n-1], dp[n-2]+cost[n-2])
# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        # 不用列表，只用两个变量存储dp[n-1]与dp[n-2]
        dp0 = 0
        dp1 = 0
        for i in range(2, l+1):
            dp0, dp1 = dp1, min(dp0+cost[i-2], dp1+cost[i-1])
        return dp1

# @lc code=end

