# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        fake_head = ListNode(None)
        cur_node = fake_head
        while l1 and l2:
            if l1.val <= l2.val:
                cur_node.next = l1
                l1 = l1.next
            else:
                cur_node.next = l2
                l2 = l2.next
            cur_node = cur_node.next
        
        if l1:
            cur_node.next = l1
        if l2:
            cur_node.next = l2
        
        return fake_head.next
