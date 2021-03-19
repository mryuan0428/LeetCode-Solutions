#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (69.27%)
# Likes:    911
# Dislikes: 0
# Total Accepted:    161.8K
# Total Submissions: 233.5K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
# 
# 注意:
# 你可以假设树中没有重复的元素。
# 
# 例如，给出
# 
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 
# 返回如下的二叉树：
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 前：【root 左子 右子】
        # 中：【左子 root 右子】
        l = len(preorder)
        if l == 0: return None
        root = TreeNode(val = preorder[0])
        
        l_left = 0 # 左子树长度
        while l_left < l:
            if inorder[l_left] == preorder[0]:
                break
            else: l_left += 1
        
        l_right = l - l_left - 1 # 右子树长度
        root.left = self.buildTree(preorder[1:1+l_left], inorder[0:l_left])
        root.right = self.buildTree(preorder[1+l_left:l], inorder[l_left+1:l])
        return root

# @lc code=end

