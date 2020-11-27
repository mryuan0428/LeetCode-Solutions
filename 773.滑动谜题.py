#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#
# https://leetcode-cn.com/problems/sliding-puzzle/description/
#
# algorithms
# Hard (61.37%)
# Likes:    103
# Dislikes: 0
# Total Accepted:    5.3K
# Total Submissions: 8.6K
# Testcase Example:  '[[1,2,3],[4,0,5]]'
#
# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
# 
# 一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
# 
# 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
# 
# 给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
# 
# 示例：
# 
# 
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
# 
# 
# 
# 输入：board = [[1,2,3],[5,4,0]]
# 输出：-1
# 解释：没有办法完成谜板
# 
# 
# 
# 输入：board = [[4,1,2],[5,0,3]]
# 输出：5
# 解释：
# 最少完成谜板的最少移动次数是 5 ，
# 一种移动路径:
# 尚未移动: [[4,1,2],[5,0,3]]
# 移动 1 次: [[4,1,2],[0,5,3]]
# 移动 2 次: [[0,1,2],[4,5,3]]
# 移动 3 次: [[1,0,2],[4,5,3]]
# 移动 4 次: [[1,2,0],[4,5,3]]
# 移动 5 次: [[1,2,3],[4,5,0]]
# 
# 
# 
# 输入：board = [[3,2,4],[1,5,0]]
# 输出：14
# 
# 
# 提示：
# 
# 
# board 是一个如上所述的 2 x 3 的数组.
# board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列.
# 
# 
#

# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        Queue = []
        visited = set()

        n = len(board)
        m = len(board[0])
        
        broadl = [] # 一维board 
        for i in range(n):
            for j in range(m):
                broadl.append(str(board[i][j]))

        target = []
        for i in range(1, n*m):
            target.append(str(i))
        target.append('0')
        target = "".join(target)

        # 转str, 节约空间
        Queue.append("".join(broadl))
        visited.add("".join(broadl))

        # 获取合法的neighbors
        def Valid_Neighbors(curNode):
            neighbors = []
            curNode = toList(curNode)
            index = curNode.index('0')
            
            # 获得'0'的位置，便于确定neighbors
            row = index // m
            column = index % m

            if row != 0: # 有上边的邻居
                upNode = curNode[:]
                upNode[index-m] = upNode[index]
                upNode[index] = curNode[index-m]
                neighbors.append("".join(upNode))
            if row != n-1: # 有下边的邻居
                downNode = curNode[:]
                downNode[index+m] = downNode[index]
                downNode[index] = curNode[index+m]
                neighbors.append("".join(downNode))
            if column != 0: # 有左边的邻居
                leftNode = curNode[:]
                leftNode[index-1] = leftNode[index]
                leftNode[index] = curNode[index-1]
                neighbors.append("".join(leftNode))
            if column != m-1: # 有右边邻居
                rightNode = curNode[:]
                rightNode[index+1] = rightNode[index]
                rightNode[index] = curNode[index+1]
                neighbors.append("".join(rightNode))
            return neighbors


        def toList(node): # 字符串转List
            nodel = []
            for i in range(len(node)):
                nodel.append(node[i])
            return nodel

        step = 0
        while(len(Queue) > 0):
            sz = len(Queue)
            
            while(sz > 0): # 遍历该层节点
                sz -= 1 # 从大到小遍历，这样pop后边的之后，不影响前边的！！！！
                
                curNode = Queue[sz]
                Queue.pop(sz)

                if curNode == target:
                    return step

                for i in Valid_Neighbors(curNode):
                    if i not in visited:
                        Queue.append(i)
                        visited.add(i)
            step += 1
        return -1

# @lc code=end

