#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (47.45%)
# Likes:    1242
# Dislikes: 0
# Total Accepted:    100.8K
# Total Submissions: 212.1K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


# 思路1：暴力：O(n^2)
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max = nums[0]
        for i in range(n):
            
            if nums[i] <= 0: #跳过开头是负数的，解决超时问题
                if nums[i] > max: #避免全负序列
                    max = nums[i]
                continue
            tmp = 0
            for j in range(i,n):
                tmp += nums[j]
                if tmp > max:
                    max = tmp

        return max

Time Limit Exceeded
201/202 cases passed (N/A)

Accepted
202/202 cases passed (7324 ms)
Your runtime beats 5.06 % of python3 submissions
Your memory usage beats 94.74 % of python3 submissions (14.2 MB)
'''

# 学习新方法：
# 动态规划：
'''
假设 nums 数组的长度是n，下标从0到n−1。
用 a_i 代表 nums[i]，用 f(i) 代表以第 i 个数结尾的「连续子数组的最大和」，那么很显然答案就是：
max { f(i) }, 0≤i≤n−1
因此只需要求出每个位置的 f(i)，然后返回 f 数组中的最大值即可。

如何求 f(i) 呢？我们可以考虑 a_i单独成为一段，还是加入 f(i−1) 对应的那一段
这取决于 a_i 和 f(i-1) + a_i的大小可以写出这样的动态规划转移方程：
f(i) = max { f(i - 1) + a_i, a_i }
不难给出一个时间复杂度 O(n)、空间复杂度O(n)的实现'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1]+nums[i], nums[i])
        return max(nums)

