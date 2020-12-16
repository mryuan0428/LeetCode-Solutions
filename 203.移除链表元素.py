#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (46.69%)
# Likes:    498
# Dislikes: 0
# Total Accepted:    119.3K
# Total Submissions: 255.6K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
# 
# 示例:
# 
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        # p_head指向第一个不为val的结点，且不为空
        p_head = head
        while p_head and p_head.val == val:
            p_head = p_head.next
        if not p_head: return p_head
        # 若不尽兴上边的操作，则申请哨兵节点！！！

        head = p_head # 最终返回head
        while p_head.next: #next不为空
            if p_head.next.val == val:
                p_head.next = p_head.next.next
            else:
                p_head = p_head.next
        
        return head


# @lc code=end

