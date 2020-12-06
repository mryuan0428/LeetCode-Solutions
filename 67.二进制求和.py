#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (54.34%)
# Likes:    526
# Dislikes: 0
# Total Accepted:    138.8K
# Total Submissions: 255.3K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 
# 输入为 非空 字符串且只包含数字 1 和 0。
# 
# 
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
# 
# 
# 提示：
# 
# 
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
# 
# 
#

# @lc code=start
# 1: 转int 10进制 相加 转2进制 
# 2: 自己实现2进制加法
class Solution:
    def method1(self, a, b):
        x, y = 0, 0
        l1, l2 = len(a), len(b)
        for i in range(l1):
            k = l1 - i - 1
            x += int(a[k]) * (2 ** i)
        for i in range(l2):
            k = l2 - i - 1
            y += int(b[k]) * (2 ** i)
        return str(bin(x+y))[2:]
    
    def method2(self, a, b):
        if len(a) > len(b):
            b = '0' * (len(a)-len(b)) + b
        elif len(a) < len(b):
            a = '0' * (len(b)-len(a)) + a
        
        c = 0 # 进位
        # 结果保存在res
        res = ''
        for i in range(len(a)):
            k = len(a) - i - 1
            x, y = int(a[k]), int(b[k])
            s = x + y + c
            if s > 1:
                res = str(s % 2) + res
                c = 1
            else:
                res = str(s) + res
                c = 0
        if c == 1: return '1'+res
        return res


    def addBinary(self, a, b):
        return self.method2(a, b)

#s = Solution()
#s.addBinary("1010", "1011")


# @lc code=end

