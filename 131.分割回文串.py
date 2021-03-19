#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (70.47%)
# Likes:    624
# Dislikes: 0
# Total Accepted:    88.7K
# Total Submissions: 121.9K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
# 
# 回文串 是正着读和反着读都一样的字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
# 
# 
# 示例 2：
# 
# 
# 输入：s = "a"
# 输出：[["a"]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由小写英文字母组成
# 
# 
#
# 回溯法
# @lc code=start
class Solution:
    def partition(self, s: str):
        l = len(s)
        if l == 1: return [[s]]
        res = []
        resi = [] #一个可能的分割方法

        def isHuiwen(si):
            i = 0
            while i <= len(si)-i-1:
                if si[i] != si[len(si)-i-1]: return False
                i += 1
            return True

        def backtrace(r):
            if r == l: 
                res.append(resi.copy()) # 此时前边分到了l-1已经是一个正确的分割了
                # !!!!!必须加copy 否则 resi.pop(-1) res中也会改变！！！！
            else: # 判断这一次的分割方式
                for i in range(r+1,l+1): # i r+1 -> l ==> r -> l-1 分割 
                    if isHuiwen(s[r:i]): 
                        resi.append(s[r:i])
                        backtrace(i)
                        resi.pop(-1)
        
        backtrace(0)
        return res
#s = Solution()
#s.partition('aab')
# @lc code=end

