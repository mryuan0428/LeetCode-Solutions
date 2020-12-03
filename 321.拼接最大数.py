#
# @lc app=leetcode.cn id=321 lang=python3
#
# [321] 拼接最大数
#
# https://leetcode-cn.com/problems/create-maximum-number/description/
#
# algorithms
# Hard (32.62%)
# Likes:    254
# Dislikes: 0
# Total Accepted:    12.2K
# Total Submissions: 30.3K
# Testcase Example:  '[3,4,6,5]\n[9,1,2,5,8,3]\n5'
#
# 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n)
# 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
# 
# 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
# 
# 说明: 请尽可能地优化你算法的时间和空间复杂度。
# 
# 示例 1:
# 
# 输入:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# 输出:
# [9, 8, 6, 5, 3]
# 
# 示例 2:
# 
# 输入:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# 输出:
# [6, 7, 6, 0, 4]
# 
# 示例 3:
# 
# 输入:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# 输出:
# [9, 8, 9]
# 
#
# 思路：若是1个数组 ～ 问题402
# nums1 取 i 位 单调递减栈；nums2 取 k-i 位 单调栈
# 然后合并
# O(k*(n+m+k^2)) (k^2: k次合并，meici比较k次)

# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        l1 = len(nums1)
        l2 = len(nums2)
        res = [0] * k

        for i in range(k+1):
            if l1 >= i and l2 >= k-i:
                tmp = self.merge(self.getMaxSubNumber(nums1, i), self.getMaxSubNumber(nums2, k-i))
                if res < tmp:
                    res = tmp[:]
        
        return res


    def getMaxSubNumber(self, nums, k):
        if k == 0: return []
        elif k == len(nums): return nums[:] # 不能return nums，否则merge的时候，pop原列表
        stack = []
        stack.append(nums[0])
        n = len(nums)
        
        rm = n - k # 保留k位，移掉rm位！！！！ 判断的时候要看rm>0

        for num in nums[1:]:
            while stack and stack[-1] < num and rm > 0:
                stack.pop()
                rm -= 1
            stack.append(num)
        
        return stack[:k]


    def merge(self, subnum1, subnum2):
        num = []

        while subnum1 or subnum2: # subnum1, subnum2不全为空
            if subnum1 > subnum2:
                num.append(subnum1[0])
                subnum1.pop(0)
            else:
                num.append(subnum2[0])
                subnum2.pop(0)
        
        return num

# @lc code=end

