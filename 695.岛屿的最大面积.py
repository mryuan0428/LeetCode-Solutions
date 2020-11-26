#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
# https://leetcode-cn.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (64.20%)
# Likes:    397
# Dislikes: 0
# Total Accepted:    67.4K
# Total Submissions: 105K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。
# 
# 一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被
# 0（代表水）包围着。
# 
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
# 
# 
# 
# 示例 1:
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# 
# 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
# 
# 示例 2:
# 
# [[0,0,0,0,0,0,0,0]]
# 
# 对于上面这个给定的矩阵, 返回 0。
# 
# 
# 
# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。
# 
#

# @lc code=start
# 最大深度搜索
class Solution:
    def maxAreaOfIsland(self, grid):
        # 特殊情况判断:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]): 
                return 0
            if grid[i][j] == 0: return 0

            area = 1
            grid[i][j] = 0

            for x in range(4): # 0/1/2/3分别表示上下左右4个方向
                if x == 0: area += dfs(i-1, j)
                elif x == 1: area += dfs(i+1, j)
                elif x == 2: area += dfs(i, j-1)
                else: area += dfs(i, j+1)
            return area

        res = 0
        # 对每个节点dfs:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                dfsij = dfs(i,j)
                if dfsij > res:
                    res = dfsij
        
        return res


# @lc code=end

