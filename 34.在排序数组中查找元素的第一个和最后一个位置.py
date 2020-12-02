#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (40.61%)
# Likes:    740
# Dislikes: 0
# Total Accepted:    177.9K
# Total Submissions: 426.9K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 
# 进阶：
# 
# 
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 
# 示例 2：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 
# 示例 3：
# 
# 
# 输入：nums = [], target = 0
# 输出：[-1,-1]
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^9 
# nums 是一个非递减数组
# -10^9 
# 
# 
#

# @lc code=start
# 思路：先二分找到target；再左右找 l r
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    #def searchRange(self, nums, target):
        n = len(nums)
        if n == 0: return [-1, -1]
        mid = n // 2
        l, r = 0, n-1
        
        while nums[mid] != target:
            if l < r:
                if nums[mid] > target:
                    r = mid - 1
                    mid = (l+r)//2
                else: 
                    l = mid + 1
                    mid = (l+r)//2
            else: return [-1, -1]
        
        l = mid
        while l != 0:
            if nums[l] == target and nums[l-1] != target:
                break
            else: l -= 1
        r = mid
        while r != n-1:
            if nums[r] == target and nums[r+1] != target:
                break
            else: r += 1
        return [l, r]

# @lc code=end

