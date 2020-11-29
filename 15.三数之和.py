#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (30.11%)
# Likes:    2781
# Dislikes: 0
# Total Accepted:    370.6K
# Total Submissions: 1.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start
# 思路：三重循环 -> 循环+内层双指针
import random
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        # 优化版快排，快速排序
        def quickSort(l, r):
            while l < r:
                x = l
                y = r
                z = random.choice(nums[l:r+1])
                while x < y:
                    while nums[x] < z: x += 1
                    while nums[y] > z: y -= 1
                    if x<=y:
                        tmp = nums[x]
                        nums[x] = nums[y]
                        nums[y] = tmp
                        x += 1
                        y -= 1
                quickSort(l,y)
                l = x
        
        n = len(nums)
        quickSort(0,n-1)
        res = []
        for i in range(n-2): # 最外层循环
            if nums[i] > 0: break
            if i == 0 or nums[i] != nums[i-1]:
                
                k = n-1
                for j in range(i+1, n-1):
                    if (j == i+1 or nums[j] != nums[j-1]) and j < k:

                        while nums[i] + nums[j] + nums[k] > 0 and k>j+1: 
                        #!!!!! k > j+1 才能保证k最小为k+1
                            k -= 1
                        
                        if nums[i] + nums[j] + nums[k] == 0:
                            res.append([nums[i], nums[j], nums[k]])
        return res

# @lc code=end

