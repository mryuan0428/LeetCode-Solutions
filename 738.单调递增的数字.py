#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#
# https://leetcode-cn.com/problems/monotone-increasing-digits/description/
#
# algorithms
# Medium (44.48%)
# Likes:    119
# Dislikes: 0
# Total Accepted:    17.4K
# Total Submissions: 35.5K
# Testcase Example:  '10'
#
# 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
# 
# （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）
# 
# 示例 1:
# 
# 输入: N = 10
# 输出: 9
# 
# 
# 示例 2:
# 
# 输入: N = 1234
# 输出: 1234
# 
# 
# 示例 3:
# 
# 输入: N = 332
# 输出: 299
# 
# 
# 说明: N 是在 [0, 10^9] 范围内的一个整数。
# 
#
# 思路：num -> list
# 从后往前遍历list, 找到最高位的l[i]<l[i+1], 记录flag=i
# 最后，flag+1 --, flag及后全9
# 最后, list -> num
# 为了方便, list倒序排列

# 出现bug: 332
# 修改: 
# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # num -> list
        num_list = []
        while N > 0:
            num_list.append(N % 10)
            N = N // 10
        
        # 遍历list并记录flag
        flag = -2
        for i in range(len(num_list)-1):
            if (num_list[i] < num_list[i+1]) or (num_list[i] == num_list[i+1] and flag == i-1):
                flag = i
        
        # 修改num_list
        if flag >= 0:
            num_list = [9] * (flag+1) + num_list[flag+1:]
            num_list[flag+1] -= 1

        #list -> num
        ans = 0
        bas = 1
        for c in num_list:
            ans += c * bas
            bas *= 10
        
        return ans

# @lc code=end

