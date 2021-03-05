#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (64.70%)
# Likes:    864
# Dislikes: 0
# Total Accepted:    251.7K
# Total Submissions: 389.1K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 示例 1:
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 
# 说明: 
# 
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
# 
#

# @lc code=start
# 1. 构造长为k的队列(单调), 这样可以找到最大的k个数
# 2. 基于快排的快速选择算法！！！
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums)-1, len(nums)-k)

    def quickSelect(self, nums: List[int], l, r, index):
        q = self.partition(nums, l, r)
        if q == index:
            return nums[q]
        elif q < index:
            return self.quickSelect(nums, q+1, r, index)
        else:
            return self.quickSelect(nums, l, q-1, index)
    
    def partition(self, nums, l, r):
        # 随机选择z，并放在左边，采用无优化版本的快排
        k = random.randrange(l, r+1)
        z = nums[k]
        nums[k] = nums[l]
        nums[l] = z

        while l < r:
            while l<r and nums[r]>=z: r -= 1
            if l < r:
                nums[l] = nums[r]
                l += 1
            while l<r and nums[l]<=z: l += 1
            if l < r:
                nums[r] = nums[l]
                r -= 1
        nums[l] = z
        return l


# @lc code=end

