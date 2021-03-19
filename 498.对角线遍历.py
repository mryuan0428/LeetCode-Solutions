#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#
# https://leetcode-cn.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (43.06%)
# Likes:    173
# Dislikes: 0
# Total Accepted:    31.3K
# Total Submissions: 72.7K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
# 
# 
# 
# 示例:
# 
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# 输出:  [1,2,4,7,5,3,6,8,9]
# 
# 解释:
# 
# 
# 
# 
# 
# 说明:
# 
# 
# 给定矩阵中的元素总数不会超过 100000 。
# 
# 
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix):
        if len(matrix) == 0: return []
        if len(matrix[0]) == 0: return []
        res = []
        dirc = True # 方向 斜向上
        r, c = len(matrix), len(matrix[0])
        i, j = 0, 0
        
        while True:
            res.append(matrix[i][j])
            if i == r-1 and j == c-1: # 结束
                break
            # 判断下一个:
            if dirc:
                n_i, n_j = i - 1, j + 1
                if n_j == c:
                    n_i = i + 1
                    n_j = j
                    dirc = False
                elif n_i == -1:
                    n_i = i
                    n_j = j + 1
                    dirc = False
            else:
                n_i, n_j = i + 1, j - 1
                if n_i == r:
                    n_i = i
                    n_j = j + 1
                    dirc = True
                elif n_j == -1:
                    n_i = i + 1
                    n_j = j
                    dirc = True
            i, j = n_i, n_j
        return res
#s = Solution()
#s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
# @lc code=end

