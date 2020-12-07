#
# @lc app=leetcode.cn id=861 lang=python3
#
# [861] 翻转矩阵后的得分
#
# https://leetcode-cn.com/problems/score-after-flipping-matrix/description/
#
# algorithms
# Medium (74.60%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    9.7K
# Total Submissions: 12.4K
# Testcase Example:  '[[0,0,1,1],[1,0,1,0],[1,1,0,0]]'
#
# 有一个二维矩阵 A 其中每个元素的值为 0 或 1 。
# 
# 移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
# 
# 在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。
# 
# 返回尽可能高的分数。
# 
# 
# 
# 
# 
# 
# 示例：
# 
# 输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# 输出：39
# 解释：
# 转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j] 是 0 或 1
# 
# 
#
# 贪心法：首先，行反转确保第一行均为1；然后从第1列开始，列的0数>1数时，反转列
# 优化复杂度：因为最后输出结果，因此不需要真的进行反转操作：
# n行m列: 从第1列开始，统计每列1的数量(对应行开头0的则0是1)
# 2^i 位运算
# @lc code=start
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        n = len(A)
        m = len(A[0])
        res = n * (1 << (m-1))

        for j in range(1, m):
            c = 0
            for i in range(n):
                if A[i][0]:
                    c += A[i][j]
                else: c += (1 - A[i][j])
            c = max(c, n-c) # !!!!
            res += c * (1 << (m-1-j))
        return res


# @lc code=end

