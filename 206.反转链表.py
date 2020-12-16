#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (71.13%)
# Likes:    1401
# Dislikes: 0
# Total Accepted:    391.8K
# Total Submissions: 550.8K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head

        def recursion(head):
            if not head.next: return head # 到达链表尾，反转后newhead
            else: 
                newhead = recursion(head.next) # 反转后边的链表
                head.next.next = head
                head.next = None
                return newhead
        
        def iteration(head): # 迭代法需要暂时保存结点
            pre = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre

        #return recursion(head)
        return iteration(head)
# @lc code=end

