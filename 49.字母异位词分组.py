#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (63.94%)
# Likes:    523
# Dislikes: 0
# Total Accepted:    120.4K
# Total Submissions: 188.3K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 
# 示例:
# 
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# 说明：
# 
# 
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
# 
# 
#

# @lc code=start
# 想法1: 将列表中的str 转为 tuple （O(NKlogK)）
# 维持一个dict, set -> list[str]
# 最后返回values即可
# 想法二：用一个26位长的计数表来表示str（O(NK)）没有了sorted排序
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            k = tuple(sorted(str)) #用tuple 而非 set (set无重复，不可hash // tuple 有重复/可hash，但是有顺序)
            if k in dict:
                dict[k].append(str)
            else:
                dict[k] = [str]
        return list(dict.values())

# @lc code=end

