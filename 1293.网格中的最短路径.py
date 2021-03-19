#
# @lc app=leetcode.cn id=1293 lang=python3
#
# [1293] 网格中的最短路径
#
# https://leetcode-cn.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
#
# algorithms
# Hard (35.48%)
# Likes:    110
# Dislikes: 0
# Total Accepted:    9.7K
# Total Submissions: 27.4K
# Testcase Example:  '[[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]\n1'
#
# 给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。
# 
# 如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1)
# 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1。
# 
# 
# 
# 示例 1：
# 
# 输入： 
# grid = 
# [[0,0,0],
# [1,1,0],
# ⁠[0,0,0],
# [0,1,1],
# ⁠[0,0,0]], 
# k = 1
# 输出：6
# 解释：
# 不消除任何障碍的最短路径是 10。
# 消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) ->
# (3,2) -> (4,2).
# 
# 
# 
# 
# 示例 2：
# 
# 输入：
# grid = 
# [[0,1,1],
# [1,1,1],
# [1,0,0]], 
# k = 1
# 输出：-1
# 解释：
# 我们至少需要消除两个障碍才能找到这样的路径。
# 
# 
# 
# 
# 提示：
# 
# 
# grid.length == m
# grid[0].length == n
# 1 <= m, n <= 40
# 1 <= k <= m*n
# grid[i][j] == 0 or 1
# grid[0][0] == grid[m-1][n-1] == 0
# 
# 
#

# @lc code=start
# 带状态的BFS 广度优先搜索
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R = len(grid)
        C = len(grid[0])
        if k >= R + C - 2: return R + C - 2

        queue = []
        visited = set() #也可以是3维数组
        dirs = [[-1,0],[0,-1],[1,0],[0,1]] #4个方向 neighbors

        queue.append((0,0,k))
        visited.add((0,0,k))

        step = 0
        while queue:
            l = len(queue)
            for _ in range(l):
                r, c, m = queue.pop(0)
                # 找到target
                if r == R - 1 and c == C - 1: return step
                for x, y in dirs:
                    nr, nc = r + x, c + y
                    # 判断是否出界
                    if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
                    # 判断是否能访问 或已经访问过
                    if m - grid[nr][nc] < 0: continue
                    if (nr, nc, m-grid[nr][nc]) in visited: continue
                    queue.append((nr, nc, m-grid[nr][nc]))
                    visited.add((nr, nc, m-grid[nr][nc]))
            step += 1
        return -1



# @lc code=end

