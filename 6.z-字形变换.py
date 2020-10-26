#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
# https://leetcode-cn.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (48.75%)
# Likes:    877
# Dislikes: 0
# Total Accepted:    182.5K
# Total Submissions: 372.9K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
# 
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 
# 
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
# 
# 请你实现这个将字符串进行指定行数变换的函数：
# 
# string convert(string s, int numRows);
# 
# 示例 1:
# 
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 
# 
# 示例 2:
# 
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# 
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
# 
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        l = len(s) 
        l_block = 2 * numRows - 2
        
        if l % l_block == 0:
            n_block = l // l_block
        else:
            n_block = l // l_block + 1
        
        z = ''

        #添加第一行内容
        for b in range(n_block):
            z = z + s[b*l_block]

        #添加后边几行内容
        for i in range(1, numRows-1):
            for b in range(n_block-1):
                z = z + s[b*l_block + i]
                z = z + s[(b+1)*l_block - i]
            up = (n_block-1)*l_block + i
            down = (n_block)*l_block - i
            if up < l:
                z = z + s[up]
            if down < l:
                z = z + s[down]
        
        #添加最后一行内容
        for b in range(n_block-1):
            z = z + s[b*l_block+numRows-1]
        index = (n_block - 1) * l_block + numRows - 1
        if index < l:
            z = z + s[index]
        
        return z



# @lc code=end

