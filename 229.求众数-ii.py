#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#
# https://leetcode-cn.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (44.92%)
# Likes:    339
# Dislikes: 0
# Total Accepted:    26.4K
# Total Submissions: 58.4K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
# 
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[3,2,3]
# 输出：[3]
# 
# 示例 2：
# 
# 
# 输入：nums = [1]
# 输出：[1]
# 
# 
# 示例 3：
# 
# 
# 输入：[1,1,1,3,3,2,2,2]
# 输出：[1,2]
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l == 1: return [nums[0]]
        
        res1 = nums[0]
        cnt1 = 0
        res2 = nums[0]
        cnt2 = 0
        for i in range(l):
            if cnt1 + cnt2 == 0:
                res1 = nums[i]
                cnt1 += 1
            elif cnt1 == 0:
                if nums[i] == res2:
                    cnt2 += 1
                else:
                    res1 = nums[i]
                    cnt1 += 1
            elif cnt2 == 0:
                if nums[i] == res1:
                    cnt1 += 1
                else:
                    res2 = nums[i]
                    cnt2 += 1
            else:
                if nums[i] == res1:
                    cnt1 += 1
                elif nums[i] == res2:
                    cnt2 += 1
                else:
                    cnt1 -= 1
                    cnt2 -= 1
        cnt1, cnt2 = 0, 0
        for i in range(l):
            if nums[i] == res1: cnt1 += 1
            elif nums[i] == res2: cnt2 += 1
        res = []
        if cnt1 > l//3: res.append(res1)
        if cnt2 > l//3 and res2 != res1: res.append(res2)
        return res


# @lc code=end

