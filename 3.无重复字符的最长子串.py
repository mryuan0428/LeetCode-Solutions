#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (35.90%)
# Likes:    4636
# Dislikes: 0
# Total Accepted:    740K
# Total Submissions: 2.1M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
# 示例 4:
# 
# 
# 输入: s = ""
# 输出: 0
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# s 由英文字母、数字、符号和空格组成
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l < 2: return l

        prepos = {s[0]:0}
        i, j = 0, 1
        res = 1
        while j < l:
            if s[j] not in prepos:
                prepos[s[j]] = j
                l_ij = j - i + 1
                res = l_ij if l_ij > res else res
                j += 1
            elif prepos[s[j]] < i:
                prepos[s[j]] = j
                l_ij = j - i + 1
                res = l_ij if l_ij > res else res
                j += 1
            else:
                i = prepos[s[j]] + 1
                prepos[s[j]] = j
                j += 1
        return res


# @lc code=end

