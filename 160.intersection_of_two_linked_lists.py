# https://leetcode.com/problems/intersection-of-two-linked-lists

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        a_iter = self.iterateOverTwoLists(headA, headB)
        b_iter = self.iterateOverTwoLists(headB, headA)
        
        while True:
            try:
                a = a_iter.next()
                b = b_iter.next()
            except StopIteration:
                return None
            if a is b:
                return a
        
        
    @staticmethod
    def iterateOverTwoLists(headA, headB):
        cur_head = headA
        while cur_head:
            yield cur_head
            cur_head = cur_head.next
        
        cur_head = headB
        while cur_head:
            yield cur_head
            cur_head = cur_head.next
