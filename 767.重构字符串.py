#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#
# https://leetcode-cn.com/problems/reorganize-string/description/
#
# algorithms
# Medium (43.25%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    15.3K
# Total Submissions: 34.1K
# Testcase Example:  '"aab"'
#
# 给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
# 
# 若可行，输出任意可行的结果。若不可行，返回空字符串。
# 
# 示例 1:
# 
# 
# 输入: S = "aab"
# 输出: "aba"
# 
# 
# 示例 2:
# 
# 
# 输入: S = "aaab"
# 输出: ""
# 
# 
# 注意:
# 
# 
# S 只包含小写字母并且长度在[1, 500]区间内。
# 
# 
#

# @lc code=start
''' 思路：统计各字母出现的次数 {}
    字符串长n，只要出现次数最多的字符数 <= (n+1)//2，就可以满足条件重构
    关键：怎么重构一个？
    dict：char:num；even_index=0，odd_index=1
    若num = (n+1)//2，则往 odd_index填，否则优先填even_index
'''

class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        if n < 2: return S
        
        max_num = 0
        max_char = S[0]
        char_dict = {}
        for char in S:
            if char in char_dict:
                char_dict[char] += 1
            else: char_dict[char] = 1

            if char_dict[char] > max_num: 
                max_num = char_dict[char]
                max_char = char
        
        if max_num > (n+1)//2: return ""

        res_list = ['a']*n
        even_index = 0
        odd_index = 1

        if max_num == (n+1)//2 :
            for i in range((n+1)//2): # 6: 0,1,2 / 7: 0,1,2,3
                res_list[i*2] = max_char
            char_dict.pop(max_char)

            for char in char_dict:
                for i in range(char_dict[char]):
                    res_list[odd_index] = char
                    odd_index += 2
            return ''.join(res_list)
        
        else:
            for char in char_dict:
                for i in range(char_dict[char]):
                    if odd_index < n:
                        res_list[odd_index] = char
                        odd_index += 2
                    else:
                        res_list[even_index] = char
                        even_index += 2
            return ''.join(res_list)


# @lc code=end

