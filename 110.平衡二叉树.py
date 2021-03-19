#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode-cn.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (55.36%)
# Likes:    631
# Dislikes: 0
# Total Accepted:    182.7K
# Total Submissions: 330K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 
# 本题中，一棵高度平衡二叉树定义为：
# 
# 
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：root = []
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数在范围 [0, 5000] 内
# -10^4 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 左平衡 + 右平衡 + 左右高度差不大于1
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        
        def height(node):
            if not node: return 0
            if not node.left and not node.right: return 1
            
            leftHeight = height(node.left)
            rightHeight = height(node.right)
            
            # 如果只return max(leftHeight, rightHeight) + 1，则自顶向下，复杂度高
            # 判断是否平衡
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            
            else: # 平衡的话，返回高度
                return max(leftHeight, rightHeight) + 1
        
        return height(root) > 0

# @lc code=end

