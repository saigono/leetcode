# https://leetcode.com/problems/add-two-numbers

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        cur_node = head
        r = 0
        while l1 and l2:
            s = (l1.val + l2.val + r) % 10
            r = (l1.val + l2.val + r) // 10
            cur_node.val = s
            new_node = ListNode(None)
            cur_node.next = new_node
            cur_node = new_node
            
            l1 = l1.next
            l2 = l2.next
        
        if l2 and not l1:
            l1 = l2
            
        while l1:
            s = (l1.val + r) % 10
            r = (l1.val + r) // 10
            cur_node.val = s
            new_node = ListNode(None)
            cur_node.next = new_node
            cur_node = new_node
            
            l1 = l1.next
        
        if r:
            cur_node.val = r
        cur_node = head
        while cur_node:
            if cur_node.next and cur_node.next.val is None:
                cur_node.next = None
                break
            cur_node = cur_node.next
        return head
