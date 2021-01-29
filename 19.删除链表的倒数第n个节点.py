#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (40.63%)
# Likes:    1188
# Dislikes: 0
# Total Accepted:    313K
# Total Submissions: 766.9K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 
# 进阶：你能尝试使用一趟扫描实现吗？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1], n = 1
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [1,2], n = 1
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中结点的数目为 sz
# 1 
# 0 
# 1 
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#法1: 先计算链表长度l，再删去第l-n+1个节点 （扫描两次）
#法2: 扫描一次：双指针，p1指向第1个，p2指向第n个，后移，p2最后时，p1倒数第n个

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        p2 = head
        for _ in range(n-1):
            p2 = p2.next

        if not p2.next: # 此时要删除第一个节点
            return head.next

        while p2.next.next: # p1指向待删除节点的前一节点
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return head
        
# @lc code=end

