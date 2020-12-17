#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (51.53%)
# Likes:    900
# Dislikes: 0
# Total Accepted:    186.4K
# Total Submissions: 361.8K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 
# grid[i][j] 的值为 '0' 或 '1'
# 
# 
#

# @lc code=start
class Solution:
    def numIslands(self, grid):
        '''错误：["1","1","1"],["0","1","0"],["1","1","1"] 判断（2，0）时
        cnt = 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0': continue
                else:
                    if i == 0 and j == 0: cnt += 1
                    elif i == 0 and grid[i][j-1] == '0': cnt += 1
                    elif j == 0 and grid[i-1][j] == '0': cnt += 1
                    elif grid[i-1][j] == '0' and grid[i][j-1] == '0': cnt += 1
                    else: continue
        return cnt
        '''
        # 深度优先算法: 连通的1标零
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]): return
            if grid[i][j] == '0': return
            
            grid[i][j] = '0'
            directions = [-1, 0, 1, 0, -1] # 上/右/下/左 四个方向
            for d in range(4):
                dfs(i+directions[d], j+directions[d+1])


        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)
        return cnt


# @lc code=end

