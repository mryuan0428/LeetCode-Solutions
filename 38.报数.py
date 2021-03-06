#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (52.50%)
# Likes:    313
# Dislikes: 0
# Total Accepted:    49.7K
# Total Submissions: 94.3K
# Testcase Example:  '1'
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
# 
# 注意：整数顺序将表示为一个字符串。
# 
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "1"
# 
# 
# 示例 2:
# 
# 输入: 4
# 输出: "1211"
# 
# 思路：n次循环，str0两个指针 数几个几
#
class Solution:
    def countAndSay(self, n: int) -> str:
        str0 = '1'
        if n == 1:
            return str0

        p_s, p_e =0, 0
        for i in range(n-1): # 0-n-2  n-1个
            str1 = ''
            while p_s < len(str0):
                curr = str0[p_s]
                cnt = 0
                while p_e < len(str0) and str0[p_e] == curr: #判断p_e边界
                    p_e += 1
                    cnt += 1
                #cnt为curr个数，p_e指向下一个curr开头
                str1 = str1 + str(cnt) +str(curr)
                p_s = p_e

            str0 = str1
            p_s, p_e = 0, 0
        return str0
        

