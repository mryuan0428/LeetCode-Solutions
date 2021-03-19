#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (52.44%)
# Likes:    371
# Dislikes: 0
# Total Accepted:    110.8K
# Total Submissions: 211.3K
# Testcase Example:  '[3,4,5,1,2]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] 。
# 
# 请找出其中最小的元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,4,5,1,2]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [4,5,6,7,0,1,2]
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -5000 
# nums 中的所有整数都是 唯一 的
# nums 原来是一个升序排序的数组，但在预先未知的某个点上进行了旋转
# 
# 
#

# @lc code=start
class Solution:
    # 跟右边比较，而非左边！！！
    def findMin(self, nums) -> int:
        length = len(nums)
        if length == 1: return nums[0]
        l, r = 0, length-1
        while l < r:
            mid = int(l+(r-l)//2)
            if nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
s=Solution()
s.findMin([4,5,6,7,0,1,2])
# @lc code=end

