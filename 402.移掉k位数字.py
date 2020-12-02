#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉K位数字
#
# https://leetcode-cn.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (32.75%)
# Likes:    468
# Dislikes: 0
# Total Accepted:    51.4K
# Total Submissions: 157K
# Testcase Example:  '"1432219"\n3'
#
# 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
# 
# 注意:
# 
# 
# num 的长度小于 10002 且 ≥ k。
# num 不会包含任何前导零。
# 
# 
# 示例 1 :
# 
# 
# 输入: num = "1432219", k = 3
# 输出: "1219"
# 解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
# 
# 
# 示例 2 :
# 
# 
# 输入: num = "10200", k = 1
# 输出: "200"
# 解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
# 
# 
# 示例 3 :
# 
# 
# 输入: num = "10", k = 2
# 输出: "0"
# 解释: 从原数字移除所有的数字，剩余为空就是0。
# 
# 
#
# 思路：保留n-k个数字使之最小：单调栈
# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k == 0: return num.lstrip('0') or '0'
        elif k == n: return "0"
        r = n-k
        
        stack = []
        stack.append(num[0])
        
        for i in range(1,n):
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop(-1)
                k -= 1
            
            stack.append(num[i])
        return ''.join(stack[:r]).lstrip('0') or '0'


# @lc code=end

