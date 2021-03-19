#
# @lc app=leetcode.cn id=1262 lang=python3
#
# [1262] 可被三整除的最大和
#
# https://leetcode-cn.com/problems/greatest-sum-divisible-by-three/description/
#
# algorithms
# Medium (51.57%)
# Likes:    110
# Dislikes: 0
# Total Accepted:    9.2K
# Total Submissions: 17.9K
# Testcase Example:  '[3,6,5,1,8]'
#
# 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [3,6,5,1,8]
# 输出：18
# 解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
# 
# 示例 2：
# 
# 输入：nums = [4]
# 输出：0
# 解释：4 不能被 3 整除，所以无法选出数字，返回 0。
# 
# 
# 示例 3：
# 
# 输入：nums = [1,2,3,4,4]
# 输出：12
# 解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 4 * 10^4
# 1 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # 排序 + sum求余数 + 根据余数减num
        s = sum(nums)
        re = s % 3
        if re == 0: return s
        else:
            nums.sort()
            if re == 1: # 找到最小的余数为1的 或者两个余数为2的
                y1 = -1
                y20, y21 = -1, -1
                for i in range(len(nums)):
                    if nums[i] % 3 == 1 and y1 < 0:  y1 = nums[i]
                    elif nums[i] % 3 == 2:
                        if y20 < 0: y20 = nums[i]
                        elif y21 < 0: y21 = nums[i]
                if y1 < 0: 
                    if y20 < 0 or y21 < 0: return 0
                    else: return s - y20 - y21
                else:
                    if y20 < 0 or y21 < 0: return s - y1
                    else:
                        return max(s-y1, s-y20-y21)
            else: # 余数为2,找一个余数为2的或者两个余数为1的，比较大小
                y10, y11 = -1, -1
                y2 = -1
                for i in range(len(nums)):
                    if nums[i] % 3 == 2 and y2 < 0: y2 = nums[i]
                    elif nums[i] % 3 == 1:
                        if y10 < 0: y10 = nums[i]
                        elif y11 < 0: y11 = nums[i]
                if y2 < 0:
                    if y10 < 0 or y11 < 0: return 0
                    else: return s - y10 - y11
                else:
                    if y10 < 0 or y11 < 0: return s - y2
                    else:
                        return max(s-y2,s-y10- y11)


# @lc code=end

