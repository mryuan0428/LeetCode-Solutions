#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (38.98%)
# Likes:    552
# Dislikes: 0
# Total Accepted:    232.2K
# Total Submissions: 595.8K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
# 
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 
# 输入: 4
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。
# 
# 
#
# 二分查找：找a: 使得 a^2 <= x 且 (a+1)^2 > x
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while True:
            a = (l + r) // 2
            if a ** 2 <= x:
                if (a + 1) ** 2 > x: return a
                else: l = a + 1
            else: r = a - 1
# @lc code=end

