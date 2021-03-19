#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#
# https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (50.06%)
# Likes:    278
# Dislikes: 0
# Total Accepted:    49.2K
# Total Submissions: 98.2K
# Testcase Example:  '[1,null,2,2]'
#
# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
# 
# 假定 BST 有如下定义：
# 
# 
# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树
# 
# 
# 例如：
# 给定 BST [1,null,2,2],
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
# 
# 
# 返回[2].
# 
# 提示：如果众数超过1个，不需考虑输出顺序
# 
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
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
    def findMode(self, root: TreeNode) -> List[int]:
        counter = {}
        def inorderTraversal(node):
            if not node: return
            if not node.left and not node.right: # leaf node
                counter[node.val] = counter.get(node.val,0) + 1
            else:
                inorderTraversal(node.left)
                counter[node.val] = counter.get(node.val,0) + 1
                inorderTraversal(node.right)

        inorderTraversal(root)
        counter = sorted(counter.items(), key = lambda x:x[1])
        
        res = []
        ma = counter[-1][1] # 最大出现次数
        
        for i in range(1,len(counter)+1):
            if counter[len(counter)-i][1] == ma:
                res.append(counter[len(counter)-i][0])
            else: break
        return res

# @lc code=end

