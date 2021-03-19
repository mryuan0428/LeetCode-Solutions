#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (66.65%)
# Likes:    461
# Dislikes: 0
# Total Accepted:    100K
# Total Submissions: 150K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 输入:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        resi = [] #使用列表需要回溯，使用字符串只需将其作为参数即可
        
        def backtrace(node):
            if not node: return

            if not node.left and not node.right: # node 为叶子节点！！！！！！
                res.append(resi + [str(node.val)])
            
            else:
                resi.append(str(node.val))
                
                backtrace(node.left)
                backtrace(node.right)
                
                resi.pop(-1) #回溯
        
        backtrace(root)

        return ['->'.join(resi) for resi in res]


# @lc code=end

