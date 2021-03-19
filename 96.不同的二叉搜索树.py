#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (69.36%)
# Likes:    1032
# Dislikes: 0
# Total Accepted:    107.4K
# Total Submissions: 154.8K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
# 
# 示例:
# 
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1: return 1
        res = [0] * (n+1) # 0-n
        res[0], res[1] = 1, 1
        def dp(n):
            for i in range(2, n+1):
                if i & 1 == 0: # oushu
                    for j in range(i//2):
                        res[i] += 2 * res[j] * res[i-j-1]
                else:
                    for j in range(i//2):
                        res[i] += 2 * res[j] * res[i-j-1]
                    res[i] += res[i//2] ** 2
        dp(n)
        return res[n]
#s = Solution()
#s.numTrees(3)
# @lc code=end

