#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (33.02%)
# Likes:    1328
# Dislikes: 0
# Total Accepted:    185K
# Total Submissions: 560.3K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#*******思路：先判断是否为负数，是则取反； 然后看是否溢出； 然后%10反转存序列，判断开头是不是0，输出。
#
class Solution:
    def reverse(self, x: int) -> int:
        
        flag_neg = 0

        #判断正负
        if x < 0:
            flag_neg = 1
            x = -x
        #判断是否溢出
        if x >= 2**31:
            return 0

        x_r = [0]
        res = 0 
        while x!=0 :
            res = x%10
            x = x//10
            x_r.append(res)

        if x_r==[0]:
            return 0
        
        while x_r[0]==0:
            x_r.pop(0)

        y=0
        for i in range(len(x_r)):
            y=y*10+x_r[i]
        
        #判断y是否溢出
        if flag_neg==1:
            if y > 2**31:
                return 0
            return -y
        else:
            if y >= 2**31:
                return 0
            return y


