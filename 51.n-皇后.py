#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (73.39%)
# Likes:    673
# Dislikes: 0
# Total Accepted:    89.1K
# Total Submissions: 121.5K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 
# 
# 示例：
# 
# 输入：4
# 输出：[
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 
# 
# 
# 
# 提示：
# 
# 
# 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
# 
# 
#

# @lc code=start
# 回溯法求解：判断节点符不符合要求
# 技巧：如何表示已占的列/左斜/右斜
class Solution:
    def solveNQueens(self, n: int):
        res = [] # 保存最终结果
        resi = [-1] * n # 保存一个可行解
        # 记录被占据的列/左斜/右斜
        columns = []
        diagonall = []
        diagonalr = []

        # 递归函数 判定终止时，resi转board append到res中
        def generateBoard(resi):
            board = []
            r = ['.'] * n
            for i in resi:
                r[i] = 'Q'
                board.append(''.join(r))
                r[i] = '.'
            return board
        
        # 递归函数：
        def backtrace(row):
            if row == n: # 终止条件, 说明此时0 - n-1行均有棋子
                res.append(generateBoard(resi))
            
            else:
                for i in range(n): # row行的每一列的节点进行判断
                    if i in columns or row+i in diagonall or row-i in diagonalr:
                        continue # 如果这行没有满足的节点就啥也不干
                    
                    # 如果节点i可以放棋子:
                    resi[row] = i 
                    columns.append(i)
                    diagonall.append(row+i) # 行下标与列下标之和即可明确表示左斜线
                    diagonalr.append(row-i) # 行下标与列下标之差即可明确表示右斜线

                    # 递归
                    backtrace(row+1)

                    # 回溯
                    columns.remove(i)
                    diagonall.remove(row+i)
                    diagonalr.remove(row-i)
                    # 判断该行的其他节点
        
        backtrace(0)
        return res

# @lc code=end

