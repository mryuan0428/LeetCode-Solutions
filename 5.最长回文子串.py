#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (31.86%)
# Likes:    2676
# Dislikes: 0
# Total Accepted:    376.4K
# Total Submissions: 1.2M
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
'''
动态规划：
用 P(i,j) 表示字符串s的第 i 到 j 个字母组成的串是否为回文串：
P(i,j) = true,如果子串[S_i:S_j]是回文串} / = false,其它情况

动态规划的状态转移方程：
P(i, j) = P(i+1, j-1) ∧ (S_i == S_j)
也就是说，只有 s[i+1:j-1] 是回文串，并且S_i == S_j时，s[i:j] 才会是回文串。

动态规划中的边界条件，即子串的长度为 1 或 2。长度为 1 的子串显然是个回文串；
对于长度为 2 的子串，只要它的两个字母相同，它就是一个回文串:
P(i, i) = true
P(i, i+1) = ( S_i == S_{i+1} )

最终的答案即为所有 P(i,j)=true 中j−i+1的最大值。
'''
# 注意动态规划的循环顺序！！！
# P(i, j) = P(i+1, j-1) ∧ (S_i == S_j)
# 先Pii，后Pxx+1……
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)] #二维数组记录P(i,j)
        ans = "" #可能s是空的

        for l in range(n): #每次判断的字符串的长度
            for i in range(n):
                j = i + l
                if j >= n:
                    break

                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i]==s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i]==s[j])

                if dp[i][j] and l+1 > len(ans):
                    ans = s[i:j+1] # ***** j+1 !!!!!!!!!
        return ans

