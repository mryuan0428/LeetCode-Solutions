#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (47.45%)
# Likes:    1242
# Dislikes: 0
# Total Accepted:    100.8K
# Total Submissions: 212.1K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
# 思路1：O(n^2) n^2的二维列表，也不是n^2，每行减少
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        #创建二维数组
        Lsum = []
        for i in range(n):
            Lsum.append([])

        Msum = nums[0]
        for i in range(n):
            j = i
            while j < n:
                if j == i:
                    Lsum[i].append(nums[j])
                else:
                    Lsum[i].append(Lsum[i][j-i-1]+nums[j]) #j-i-1

                if Lsum[i][j-i] >= Msum: #j-i
                    Msum = Lsum[i][j-i]
                j += 1
        
        return Msum

× Time Limit Exceeded
× 200/202 cases passed (N/A)
× Testcase: [-57,9,-72,-72,-62,45,-97,24,-39,35,-82,-4,-63,1,
-93,42,44,1,-75,-25,-87,-16,9,-59,20,5,-95,-41,4,-30,47,46,78,
52,74,93,-3,53,17,34,-34,34,-69,-21,-87,-86,-79,56,-9,-55,-69,
3,5,16,21,-75,-79,2,-39,25,72,84,-52,27,36,98,20,-90,52,-85,44,
94,25,51,-27,37,41,-6,-30,-68,15,-23,11,-79,93,-68,-78,90,11,-41,
84,59,4,-8,-44,-69,91,15,74,80,83,-12,59,-37,-54,5,34,27,87,-50,-81,8,
-90,52,-11,-1,-4,-97,0,78,87,-39,37,-32,30,70,-1,21,-38,-50,-22,-55,15,
-85,8,60,19,-81,-35,-17,-31,-40,90,-45,-88,-44,53,-15,-41,-70,-37,-77,
-33,77,-9,96,24,66,-6,85,92,72,-70,7,86,14,-32,-18,33,9,64,78,68,32,-90,
57,87,62,-58,-77,68,-19,-54,-65,-42,13,-68,58,-44,25,43,-52,-26,73,55,-63,
-13,-77,18,96,31,-40,51,-1,91,60,-44,55,22,-26,78,-10,32,-99,2,66,13,33,25,
68,-65,-32,-84,-14,-82,70,22,5,69,-59,-22,-23,0,-70,53,-32,89,85,-77,-11,
-40,77,55,68,77,-43,34,-33,66,-41,-88,-98,27,-72,-13,21,74,85,-74,21,-74,
-19,97,2,10,50,46,-1,13,69,87,72,23,20,40,1,76,-49,67,43,10,79,21,-86,83...
× Answer: 
× Stdout: '''

# 需优化时间复杂度:
# 首先将nums中连续的负数和正数各加起来，组成一个新列表
# 若全正，输出和；全负输出最小的；

'''class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        nnums = []
        s_temp = nums[0]
        if nums[0] > 0:
            sign = True
        else:
            sign = False

        for i in range(1,n):
            if nums[i] > 0:
                if sign == True:
                    s_temp += nums[i]
                else:
                    nnums.append(s_temp)
                    s_temp = nums[i]
                    sign = True
            else:
                if sign == False:
                    s_temp += nums[i]
                else:
                    nnums.append(s_temp)
                    s_temp = nums[i]
                    sign = False
        nnums.append(s_temp)##################别漏了
        #经过之前步骤，得到nnums

        n = len(nnums)    
        if n == 1:
            if nnums[0] < 0:
                return(max(nums))
            else:
                return nnums[0]

        #创建二维数组
        Lsum = []
        for i in range(n):
            Lsum.append([])

        Msum = nnums[0]
        for i in range(n):
            j = i
            while j < n:
                if j == i:
                    Lsum[i].append(nnums[j])
                else:
                    Lsum[i].append(Lsum[i][j-i-1]+nnums[j]) #j-i-1

                if Lsum[i][j-i] >= Msum: #j-i
                    Msum = Lsum[i][j-i]
                j += 1
        
        return Msum   '''
#还是超时


