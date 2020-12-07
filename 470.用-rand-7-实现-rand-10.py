#
# @lc app=leetcode.cn id=470 lang=python3
#
# [470] 用 Rand7() 实现 Rand10()
#
# https://leetcode-cn.com/problems/implement-rand10-using-rand7/description/
#
# algorithms
# Medium (51.95%)
# Likes:    135
# Dislikes: 0
# Total Accepted:    13.5K
# Total Submissions: 26K
# Testcase Example:  '1'
#
# 已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。
# 
# 不要使用系统的 Math.random() 方法。
# 
# 
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: 1
# 输出: [7]
# 
# 
# 示例 2:
# 
# 
# 输入: 2
# 输出: [8,4]
# 
# 
# 示例 3:
# 
# 
# 输入: 3
# 输出: [8,1,10]
# 
# 
# 
# 
# 提示:
# 
# 
# rand7 已定义。
# 传入参数: n 表示 rand10 的调用次数。
# 
# 
# 
# 
# 进阶:
# 
# 
# rand7()调用次数的 期望值 是多少 ?
# 你能否尽量少调用 rand7() ?
# 
# 
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
# 拒绝采样法
# 关键是 怎么从 1-7的均匀分布 -> 1-10的均匀分布
# 思路：从1-7得到 1-n的长为n的均匀分布，n能整除10即可 或者 （n-k）可整除10
class Solution:
    def rand10(self):
        # rand7: 1-7; (rand7-1)*7: 0,7,14…,42
        s = rand7() + (rand7() - 1) * 7 # 1-49均匀分布(49个数字)
        while s > 40:
            s = rand7() + (rand7() - 1) * 7
        # 直到s: 1-40
        return 1 + s % 10
        
# @lc code=end

