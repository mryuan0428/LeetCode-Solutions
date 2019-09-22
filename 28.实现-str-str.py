#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (38.89%)
# Likes:    262
# Dislikes: 0
# Total Accepted:    84.3K
# Total Submissions: 216.5K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
# 
# 示例 1:
# 
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 
# 
# 说明:
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 
# 思路：str.find函数可以实现
#      两个指针移动比较
# 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #return haystack.find(needle)

        if needle == '':
            return 0
        if len(haystack) < len(needle):
            return -1
        
        p_h, p_n = 0, 0
        while p_h <= len(haystack)-len(needle):
            if haystack[p_h] != needle[p_n]:
                p_h += 1
            else:
                flag = True
                i = 0
                for i in range(len(needle)):
                    if haystack[p_h+i] != needle[i]:
                        flag = False
                        break
                if flag == True:
                    return p_h
                else:
                    p_h += 1
        return -1       

