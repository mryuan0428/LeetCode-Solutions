#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (57.29%)
# Likes:    636
# Dislikes: 0
# Total Accepted:    113.9K
# Total Submissions: 198.6K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pl1 = l1
        pl2 = l2
        
        #head = pl1
        #end = head
        #这样不行，这样的话相当于 pl1 head end 都对应同一个节点实例
        #head和end应该创建一个新的类实例

        

        if pl1.val <= pl2.val:
            head = pl1 

        while pl1!= None && pl2 != None:

        

