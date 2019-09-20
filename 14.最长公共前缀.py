#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.79%)
# Likes:    704
# Dislikes: 0
# Total Accepted:    124.6K
# Total Submissions: 357.7K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
#
# 思路：找出最短字符串，视为总的列数;
#      再比较同列各行是否相同。
# **********row 和 col 别反了
#
'''  
  × Testcase: []
  × Answer: 
  × Stdout: ''
'''
# strs为空or stri为空 判断




class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = '' #空
        if strs == []:
            return prefix
        
        #找到最短字符串，即最长公共前缀
        column = len(strs[0])
        for stri in strs:
            length = len(stri)
            if length < column:
                column = length

        if column == 0:
            return prefix

        for col in range(column):          # col = 0 -> last one
            prev = strs[0][col]
            for row in range(len(strs)):   # row = 0->last one
                if strs[row][col] != prev: # 若不同，查找完毕，return
                    return prefix
                prev = strs[row][col]
            # 一列比较完成
            prefix = prefix + strs[row][col]
        return  prefix               

