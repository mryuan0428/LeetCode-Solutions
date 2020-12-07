#
# @lc app=leetcode.cn id=397 lang=python3
#
# [397] 整数替换
#
# https://leetcode-cn.com/problems/integer-replacement/description/
#
# algorithms
# Medium (36.93%)
# Likes:    79
# Dislikes: 0
# Total Accepted:    10.2K
# Total Submissions: 27.5K
# Testcase Example:  '8'
#
# 给定一个正整数 n ，你可以做如下操作：
# 
# 
# 如果 n 是偶数，则用 n / 2替换 n 。
# 如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
# 
# 
# n 变为 1 所需的最小替换次数是多少？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 8
# 输出：3
# 解释：8 -> 4 -> 2 -> 1
# 
# 
# 示例 2：
# 
# 
# 输入：n = 7
# 输出：4
# 解释：7 -> 8 -> 4 -> 2 -> 1
# 或 7 -> 6 -> 3 -> 2 -> 1
# 
# 
# 示例 3：
# 
# 
# 输入：n = 4
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#
# 位操作：判断奇偶 & 1；
# 除2 >> 1 (向下取整)(相当于先-1再/2)
# 但是需要判断+1 还是-1 (有时候+1会使高位0多，后续只/2，如65535)
# 广度优先搜索？ 
'''
11    -1 
111   +1 -1 均可
1111
'''
# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        def getMinRes(n):
            if n in mem: return mem[n]
            res = 0
            while n & 1 == 0: #偶数
                res += 1
                n = n >> 1
            # 变为奇数
            if n == 1: return res
            res += 2
            res += min(getMinRes((n+1)>>1), getMinRes((n-1)>>1))
            return res
        #mem = {1:0}
        #return getMinRes(n)

        res = 0
        while n != 1 and n != 3: 
            if n & 1 == 0: # 偶数
                n = n >> 1
                res += 1
            elif n & 2: # 以11结尾
                n += 1
                n = n >> 1
                res += 2
            else: # 以 01结尾
                n = n >> 1
                res += 2
        if n == 3: return res + 2
        return res


# @lc code=end

