#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
# https://leetcode-cn.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (58.99%)
# Likes:    607
# Dislikes: 0
# Total Accepted:    97.1K
# Total Submissions: 164.4K
# Testcase Example:  '"III"'
#
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
# 
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V +
# II 。
# 
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5
# 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
# 
# 
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 
# 
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
# 
# 示例 1:
# 
# 输入: "III"
# 输出: 3
# 
# 示例 2:
# 
# 输入: "IV"
# 输出: 4
# 
# 示例 3:
# 
# 输入: "IX"
# 输出: 9
# 
# 示例 4:
# 
# 输入: "LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.
# 
# 
# 示例 5:
# 
# 输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
# 
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# IV            4
# IX            9
# XL            40
# XC            90
# CD            400
# CM            900
#***思路：先查找特殊左放的两字母组合，计数然后替换掉。再找单字符
'''
新思路：从左到右单字符加起来，如果前边的字符对应阿拉伯数字小，则重新减去它，知道最后一个罗马数字
使用字典存储罗马数字对阿拉伯数字对应
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev, total = 0, 0          #前一个字符和总数
        
        for c in s:
            curr = roman[c]         #获取当前罗马字符对应的阿拉伯数值
            total += curr           #先加上去
            
            # need to subtract
            if curr > prev:         #prev初始值为0，第一次必然执行，不过没影响
                total -= 2 * prev   #后面prev为curr的前一个字符，如果小，则减去prev
            prev = curr
        return total
        

