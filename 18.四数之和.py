#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (39.38%)
# Likes:    679
# Dislikes: 0
# Total Accepted:    138K
# Total Submissions: 350.4K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 
# 注意：
# 
# 答案中不可以包含重复的四元组。
# 
# 示例：
# 
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#

# @lc code=start
import random
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
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
        quickSort(0, n-1)
        res = []
        
        for i in range(n-3):
            if i == 0 or nums[i]!=nums[i-1]: # 第一层循环

                for j in range(i+1, n-2):
                    if j == i+1 or nums[j]!=nums[j-1]: # 第二层循环

                        l = n - 1
                        for k in range(j+1, n-1):
                            if (k == j+1 or nums[k]!=nums[k-1]) and k<l:
                                
                                while nums[i]+nums[j]+nums[k]+nums[l]>target and l>k+1:
                                    l -= 1
                                if nums[i]+nums[j]+nums[k]+nums[l]==target:
                                    res.append([nums[i],nums[j],nums[k],nums[l]])
        return res

# @lc code=end

