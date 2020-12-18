#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode-cn.com/problems/valid-anagram/description/
#
# algorithms
# Easy (63.34%)
# Likes:    317
# Dislikes: 0
# Total Accepted:    188K
# Total Submissions: 296.8K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 
# 示例 1:
# 
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: s = "rat", t = "car"
# 输出: false
# 
# 说明:
# 你可以假设字符串只包含小写字母。
# 
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else: s_dict[s[i]] = 1
            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else: t_dict[t[i]] = 1
        
        if len(s_dict) != len(t_dict): return False
        
        for c in s_dict.keys():
            if c in t_dict.keys() and t_dict[c] == s_dict[c]:
                continue
            else: return False
        
        return True
        
# @lc code=end

