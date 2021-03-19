#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (74.67%)
# Likes:    877
# Dislikes: 0
# Total Accepted:    359.7K
# Total Submissions: 480K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1]
# 输出：[1]
# 
# 
# 示例 4：
# 
# 
# 输入：root = [1,2]
# 输出：[2,1]
# 
# 
# 示例 5：
# 
# 
# 输入：root = [1,null,2]
# 输出：[1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [0, 100] 内
# -100 
# 
# 
# 
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def inorderTraversal(node): # 递归
            if node != None:
                inorderTraversal(node.left)
                res.append(node.val)
                inorderTraversal(node.right)
        
        #inorderTraversal(root)

        stack = []
        poptimes = {}
        if root: stack.append(root)
        while len(stack) != 0:
            node = stack.pop()
            if node not in poptimes: 
                poptimes[node] = 1
                stack.append(node)
                if node.left: stack.append(node.left)
            else:
                res.append(node.val)
                if node.right: stack.append(node.right)


        return res
# @lc code=end

