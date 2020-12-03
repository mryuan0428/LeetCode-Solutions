#
# @lc app=leetcode.cn id=1081 lang=python3
#
# [1081] 不同字符的最小子序列
#
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (53.47%)
# Likes:    60
# Dislikes: 0
# Total Accepted:    6.4K
# Total Submissions: 12K
# Testcase Example:  '"bcabc"'
#
# 返回字符串 text 中按字典序排列最小的子序列，该子序列包含 text 中所有不同字符一次。
# 
# 
# 
# 示例 1：
# 
# 输入："cdadabcc"
# 输出："adbc"
# 
# 
# 示例 2：
# 
# 输入："abcd"
# 输出："abcd"
# 
# 
# 示例 3：
# 
# 输入："ecbacba"
# 输出："eacb"
# 
# 
# 示例 4：
# 
# 输入："leetcode"
# 输出："letcod"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= text.length <= 1000
# text 由小写英文字母组成
# 
# 
# 
# 
# 注意：本题目与 316 https://leetcode-cn.com/problems/remove-duplicate-letters/ 相同
# 
#

# @lc code=start
# 本题目与 316 相同
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        c_set = set()
        c_count = {}

        for c in s:
            if c in c_count:
                c_count[c] += 1
            else: c_count[c] = 1
        
        stack.append(s[0])
        c_set.add(s[0])
        c_count[s[0]] -= 1

        for c in s[1:]:
            if c not in c_set:
                while stack and stack[-1] > c and c_count[stack[-1]] > 0:
                    c_set.remove(stack[-1])
                    stack.pop()
                
                stack.append(c)
                c_set.add(c)
            c_count[c] -= 1
        
        return ''.join(stack)
                

# @lc code=end

