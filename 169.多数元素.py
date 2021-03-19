#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (65.15%)
# Likes:    822
# Dislikes: 0
# Total Accepted:    243.1K
# Total Submissions: 373.1K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 
# 
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# 
#
# dict计数 / 
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        n = len(nums)
        target = n // 2
        cnt = {}
        for i in range(n):
            if nums[i] in cnt:
                cnt[nums[i]] += 1
            else: cnt[nums[i]] = 1
            if cnt[nums[i]] > target:
                return nums[i]
        '''
        # 摩尔投票
        l = len(nums)
        if l == 1: return nums[0]

        res = nums[0]
        cnt = 1
        for i in range(1,l):
            if cnt == 0:
                cnt += 1
                res = nums[i]
            elif res == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        return res

# @lc code=end

