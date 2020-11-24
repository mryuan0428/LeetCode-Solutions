#
# @lc app=leetcode.cn id=906 lang=python3
#
# [906] 超级回文数
#
# https://leetcode-cn.com/problems/super-palindromes/description/
#
# algorithms
# Hard (25.06%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 6K
# Testcase Example:  '"4"\n"1000"'
#
# 如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。
# 
# 现在，给定两个正整数 L 和 R （以字符串形式表示），返回包含在范围 [L, R] 中的超级回文数的数目。
# 
# 
# 
# 示例：
# 
# 输入：L = "4", R = "1000"
# 输出：4
# 解释：
# 4，9，121，以及 484 是超级回文数。
# 注意 676 不是一个超级回文数： 26 * 26 = 676，但是 26 不是回文数。
# 
# 
# 
# 提示：
# 
# 
# 1 <= len(L) <= 18
# 1 <= len(R) <= 18
# L 和 R 是表示 [1, 10^18) 范围的整数的字符串。
# int(L) <= int(R)
# 
# 
# 
# 
#

# @lc code=start
# 想法1: 判断 sqrt(L)~sqrt(R) 是否为回文数，若是，再判断其平方是不是回文数
# 超时
'''
class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        res = 0
        L = int(L)
        R = int(R)
        l = int(L ** 0.5)
        r = int(R ** 0.5)
        for i in range(l, r+1):
            if str(i) == str(i)[::-1]: ######### 倒序 
                if str(i ** 2) == str(i ** 2)[::-1]:
                    res += 1
        return res
'''
# 改进：从判断回文数到主动构造回文数
"""L 和 R 是表示 [1, 10^18) 范围的整数的字符串
先判断l-r [1,10^9] 是否回文
不去按个判断(超时), 令k=[0,100000],构造回文 k(-k) (分奇数长度和偶数长度)
判断 k(-k) 是否在l-r之间，并判断其平方是否为回文数
"""
class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        l = int(int(L) ** 0.5)
        r = int(int(R) ** 0.5)
        res = 0
        
        # 回文数k(-k)长为奇数
        for k in range(10 ** (len(str(l))//2), 10 ** 5):
            pal = int(str(k)+(str(k)[-2::-1]))
            if pal > r:
                break
            if l <= pal and str(pal ** 2) == str(pal ** 2)[::-1]: # 判断回文数
                res += 1
        
        # 回文数k(-k)长为偶数
        for k in range((10 ** (len(str(l))//2))//10, 10 ** 5):
            pal = int(str(k)+(str(k)[::-1]))
            if pal > r:
                break
            if l <= pal and str(pal ** 2) == str(pal ** 2)[::-1]:
                res += 1
        return res


# @lc code=end

