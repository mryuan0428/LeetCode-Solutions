#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (46.61%)
# Likes:    6329
# Dislikes: 0
# Total Accepted:    562.9K
# Total Submissions: 1.2M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 
# 示例:
# 
# 给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 
# 
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_index = [(v, index) for index, v in enumerate(nums)] 
        #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        
        nums_index.sort()
        '''
        获取列表的第二个元素
        def takeSecond(elem):
            return elem[1]
        random = [(2, 2), (3, 4), (4, 1), (1, 3)]
        指定第二个元素排序
        random.sort(key=takeSecond)
        '''
        
        begin, end = 0, len(nums) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1
        #除sort排序外，时间复杂度O(n)
        

