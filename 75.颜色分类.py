#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
# https://leetcode-cn.com/problems/sort-colors/description/
#
# algorithms
# Medium (57.77%)
# Likes:    815
# Dislikes: 0
# Total Accepted:    184K
# Total Submissions: 318.3K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [0]
# 输出：[0]
# 
# 
# 示例 4：
# 
# 
# 输入：nums = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 
# nums[i] 为 0、1 或 2
# 
# 
# 
# 
# 进阶：
# 
# 
# 你可以不使用代码库中的排序函数来解决这道题吗？
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
# 
# 
#

# @lc code=start
class Solution:
    def onepoint(self, nums):
        ptr = 0 # 找0并放置在ptr位置
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[ptr], nums[i] = nums[i], nums[ptr]
                ptr += 1
        
        # ptr指向第一个不为0的
        if ptr < len(nums):
            for i in range(ptr, len(nums)):
                if nums[i] == 1:
                    nums[ptr], nums[i] = nums[i], nums[ptr]
                    ptr += 1
    
    def twopoint(self, nums):
        ptr0, ptr1 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[ptr0], nums[i] = nums[i], nums[ptr0]
                if ptr1 > ptr0: # ptr0把1换到i了
                    nums[ptr1], nums[i] = nums[i], nums[ptr1]
                ptr0 += 1
                ptr1 += 1
            elif nums[i] == 1:
                nums[ptr1], nums[i] = nums[i], nums[ptr1]
                ptr1 += 1


    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 单指针
        #self.onepoint(nums)

        # 双指针
        self.twopoint(nums)
    
# @lc code=end

