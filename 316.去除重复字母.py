#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
# https://leetcode-cn.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Medium (43.11%)
# Likes:    286
# Dislikes: 0
# Total Accepted:    25.8K
# Total Submissions: 59.9K
# Testcase Example:  '"bcabc"'
#
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
# 
# 注意：该题与 1081
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters
# 相同
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "bcabc"
# 输出："abc"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbacdcbc"
# 输出："acdb"
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 由小写英文字母组成
# 
# 
#
# 思路1：变体单调栈（重复时才决定pop） + 字典记录重复
# 思路2：思路1错误不应该重复时决定pop！！！而是元素入栈时，pop栈顶元素前判断其是否还会在后续入栈
# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        c_set = set() # 用来判断当前元素是否已在栈内，已在则pass  O(1)
        
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
                # 当栈非空，栈顶元素>当前元素，栈顶元素后续还有时，pop栈顶元素
                while stack and stack[-1] > c and  c_count[stack[-1]] > 0:
                    c_set.remove(stack[-1])
                    stack.pop()

                stack.append(c)
                c_set.add(c)

            c_count[c] -= 1 # 无论c在不在c_set，都要 --
            
        return ''.join(stack)


'''错误思路1：
    def removeDuplicateLetters(self, s):
        stack = []
        c_dict = {}
        c_index = 0
        stack.append(s[0])
        c_dict[s[0]] = c_index

        for c in s[1:]:
            if c not in c_dict:
                stack.append(c)
                c_index += 1
                c_dict[c] = c_index
            else:
                # if c > stack[-1]: 错误！应stack中原c与其后一个字符比较决定 ->（也不对 bcabc）
                
                c0_index = c_dict[c]
                # 原c不是最后一个，且原c > 后邻字母，则pop原c & 更新dict，否则continue
                if c0_index != c_index and stack[c0_index] > stack[c0_index+1]:
                    stack.pop(c0_index)

                    for char in c_dict:
                        if c_dict[char] > c0_index:
                            c_dict[char] -= 1
                    
                    stack.append(c)
                    c_dict[c] = c_index
        
        return ''.join(stack)
'''
# @lc code=end

