# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 
# @param root TreeNode类 
# @param sum int整型 
# @return int整型二维数组
#
class Solution:
    def pathSum(self , root , sum ):
        res = []
        resi = [] #回溯，相当于栈
        s = 0
        
        def backtrace(node, s):
            if not node: return

            # !!! node为None，它的父节点不一定是叶子
            if not node.left and not node.right:
                if s+node.val == sum:
                    res.append(resi+[node.val])
            
            else:
                #if s + node.val < sum: 
                # # val可能为负数！
                s += node.val
                resi.append(node.val)

                backtrace(node.left, s)
                backtrace(node.right, s)

                s -= node.val
                resi.pop(-1)
        
        backtrace(root, s)

        return res




