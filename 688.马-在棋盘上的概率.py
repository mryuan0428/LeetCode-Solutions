#
# @lc app=leetcode.cn id=688 lang=python3
#
# [688] “马”在棋盘上的概率
#
# https://leetcode-cn.com/problems/knight-probability-in-chessboard/description/
#
# algorithms
# Medium (50.35%)
# Likes:    104
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 12.1K
# Testcase Example:  '3\n2\n0\n0'
#
# 已知一个 NxN 的国际象棋棋盘，棋盘的行号和列号都是从 0 开始。即最左上角的格子记为 (0, 0)，最右下角的记为 (N-1, N-1)。 
# 
# 现有一个 “马”（也译作 “骑士”）位于 (r, c) ，并打算进行 K 次移动。 
# 
# 如下图所示，国际象棋的 “马” 每一步先沿水平或垂直方向移动 2 个格子，然后向与之相垂直的方向再移动 1 个格子，共有 8
# 个可选的位置。
# 
# 
# 
# 
# 
# 
# 
# 现在 “马” 每一步都从可选的位置（包括棋盘外部的）中独立随机地选择一个进行移动，直到移动了 K 次或跳到了棋盘外面。
# 
# 求移动结束后，“马” 仍留在棋盘上的概率。
# 
# 
# 
# 示例：
# 
# 输入: 3, 2, 0, 0
# 输出: 0.0625
# 解释: 
# 输入的数据依次为 N, K, r, c
# 第 1 步时，有且只有 2 种走法令 “马” 可以留在棋盘上（跳到（1,2）或（2,1））。对于以上的两种情况，各自在第2步均有且只有2种走法令 “马”
# 仍然留在棋盘上。
# 所以 “马” 在结束后仍在棋盘上的概率为 0.0625。
# 
# 
# 
# 
# 注意：
# 
# 
# N 的取值范围为 [1, 25]
# K 的取值范围为 [0, 100]
# 开始时，“马” 总是位于棋盘上
# 
# 
#

# @lc code=start
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0: return 1
        if N < 3: return 0

        move = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

        '''
        # 递归超时，N=8 K=30就不行了
        def prob1step(x,y,K):
            if K == 0: return 1
            prob = 0
            for i, j in move:
                if 0 <= x+i < N and 0 <= y+j < N:
                    prob += prob1step(x+i,y+j,K-1) * 0.125
            return prob
        
        return prob1step(r,c,K)
        '''
        # 自底向上，动态规划 dp[i][j][k] 在ij跳k步还在棋盘的概率 ～ 其他位置 跳k-1步还在棋盘上的概率
        dp1 = [[1] * N for _ in range(N)] #跳0步还在棋盘上的概率
        dp2 = [[0] * N for _ in range(N)]
        
        for _ in range(K-1): # K-1步，最后一步不用全部计算
            for i in range(N):
                for j in range(N):
                    for x, y in move:
                        if 0 <= x+i < N and 0 <= y+j < N:
                            dp2[i][j] += dp1[x+i][y+j]/8
            dp1 = dp2.copy()
            dp2 = [[0] * N for _ in range(N)]
        
        # 最后一步
        res = 0
        for x, y in move:
            if 0 <= x+r < N and 0 <= y+c < N:
                res += dp1[x+r][y+c]/8
        return res
#s = Solution()
#s.knightProbability(3,3,0,0)
# @lc code=end

