# https://leetcode.com/problems/odd-even-linked-list/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        odd_head = ListNode(head.val)
        odd_cur = odd_head
        iter_head = head
        while iter_head:
            if not iter_head.next or not iter_head.next.next:
                break
            odd_cur.next = ListNode(iter_head.next.next.val)
            odd_cur = odd_cur.next
            iter_head = iter_head.next.next
        
        even_head = ListNode(head.next.val)
        even_cur = even_head
        iter_head = head.next
        while iter_head:
            if not iter_head.next or not iter_head.next.next:
                break
            even_cur.next = ListNode(iter_head.next.next.val)
            even_cur = even_cur.next
            iter_head = iter_head.next.next
        
        odd_cur.next = even_head
        
        return odd_head
