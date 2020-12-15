#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.82%)
# Likes:    631
# Dislikes: 0
# Total Accepted:    169.6K
# Total Submissions: 370.1K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 
# 
# 示例：
# 
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
# 
# 
#
# 先快速排序，再利用三数之和的方法遍历
# @lc code=start
class Solution:
    def quickSort(l, r):
        while l < r:
            x, y = l, r
            k = nums[l]
            while x < y:
                while k > nums[x]: x += 1 # 没有=，因为可能超出index范围！！！
                while k < nums[y]: y -= 1
                if x <= y: # 有等号，为了x++, y--
                    tmp = nums[x]
                    nums[x] = nums[y]
                    nums[y] = tmp
                    x += 1
                    y -= 1
            quickSort(l, y)
            l = x


    def threeSumClosest(self, nums, target):
        def quickSort(l, r):
            while l < r:
                x, y = l, r
                k = nums[l]
                while x < y:
                    while k > nums[x]: x += 1 # 没有=，因为可能超出index范围！！！
                    while k < nums[y]: y -= 1
                    if x <= y: # 有等号，为了x++, y--
                        tmp = nums[x]
                        nums[x] = nums[y]
                        nums[y] = tmp
                        x += 1
                        y -= 1
                quickSort(l, y)
                l = x
        
        n = len(nums)
        dis = 1e5
        ans = target
        quickSort(0, n-1)

        # O(n^2)遍历找dis最小的
        for i in range(n-2):
            if i == 0 or nums[i] != nums[i-1]:
                j = i + 1
                k = n - 1
                while j < k:
                    dif = nums[i]+nums[j]+nums[k]-target
                    if dif == 0: return target
                    if abs(dif) < dis:
                        dis = abs(dif)
                        ans = nums[i]+nums[j]+nums[k]
                    if dif > 0: k -= 1
                    else: j += 1
        
        return ans

#s=Solution()
#s.threeSumClosest([-1,2,1,-4], 1)
# @lc code=end

