# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    @staticmethod
    def merge2Lists(l1: List[ListNode], l2: List[ListNode]):
        root = ListNode(None)
        cur_node = root
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
        
        return root.next
                    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [l for l in lists if l]
        if not lists:
            return None
        
        while len(lists) > 1:
            new_lists = []
            while len(lists) > 1:
                new_lists.append(self.merge2Lists(lists.pop(-1), lists.pop(-1)))
            lists = new_lists + lists
            
        return lists[0]
