"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Result:
Runtime: 428 ms, faster than 6.55% of Python3 online submissions for Sort List.
Memory Usage: 23.2 MB, less than 37.74% of Python3 online submissions for Sort List.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        elif head.next is None:
            return head
        
        temp = slow = fast = head
        
        # slow points to middle of list and fast points to end of list
        while fast is not None and fast.next is not None:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        
        temp.next = None        # this is to prevent left linked list from viewing entire linked list again (looping): left == head --> temp, right == slow --> end
        #Recurse to find sub sorted linked lists
        left = self.sortList(head)
        right = self.sortList(slow)
        
        # Typical left and right merge sort
        newHead = newCurr = ListNode(0)
        
        while right is not None and left is not None:
            
            if right.val <= left.val:
                newCurr.next = ListNode(right.val)
                right = right.next
                newCurr = newCurr.next
            else:
                newCurr.next = ListNode(left.val)
                left = left.next
                newCurr = newCurr.next
        
        #add remaining in either left/right lists
        while right:
            newCurr.next = ListNode(right.val)
            right = right.next
            newCurr = newCurr.next
        
        while left:
            newCurr.next = ListNode(left.val)
            left = left.next
            newCurr = newCurr.next
        
        #head is just dummy listNode so return actual value
        return newHead.next