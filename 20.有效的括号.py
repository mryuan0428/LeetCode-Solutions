#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (39.59%)
# Likes:    1074
# Dislikes: 0
# Total Accepted:    126.4K
# Total Submissions: 319K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
# 思路：从左往右读字符串，左括号入栈，，遇到右括号判读栈顶是否为配对左括号<dict>；
#      是则出站，继续读取；否则输出false;
#      结束条件：字符串读完，栈为空才行。
#
class Solution:
    def isValid(self, s: str) -> bool:
        Left = ['(', '[', '{']
        #Right= [')', ']', '}']
        isLeft = {')':'(', '}':'{', ']':'['}
        
        stack = []
        for punc in s:   #punctuation 标点符号
            if punc in Left:
                stack.append(punc)
            else:
                if stack == []: #先判断栈是否为空
                    return False
                elif stack[len(stack)-1] == isLeft[punc]: #配对成功，出栈
                    stack.pop()
                else:
                    return False
        
        #全部判断完后还要看栈是否为空
        if stack == []:
            return True
        else:
            return False



