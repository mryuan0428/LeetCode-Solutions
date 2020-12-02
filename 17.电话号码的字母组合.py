#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (55.54%)
# Likes:    1022
# Dislikes: 0
# Total Accepted:    197.9K
# Total Submissions: 356.3K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 示例:
# 
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
# 
#
# 思路：如何实现 len(digits)层 for循环嵌套
# 2. *****回溯法*******
# 1. 列表推导式！！！！ --------- 确定层数的for循环：保存中间状态！！！！
# @lc code=start
class Solution:
    #def letterCombinations(self, digits: str) -> List[str]:
    def letterCombinations(self, digits):
        if not digits: return []
        
        dial_dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno",
                     '7':"pqrs",'8':"tuv",'9':"wxyz"}

        def method1():
            res = ['']
            new_res = []
            for digit in digits:
                for pre in res:
                    for char in dial_dict[digit]:
                        new_res.append(pre + char)
                res = new_res[:]
                new_res = []
            return res
        
        def method1_2():
            res = ['']
            for digit in digits:
                res = [ pre + char for pre in res for char in dial_dict[digit]]
            return res
        
        res = []
        combination = []
        n = len(digits)
        
        def backtrace(r):
            if r == n: res.append(''.join(combination))
            else: 
                for char in dial_dict[digits[r]]:
                    combination.append(char)
                    backtrace(r+1)
                    combination.pop(-1)

        backtrace(0)
        
        return res

#s = Solution()
#s.letterCombinations('23')

# @lc code=end

