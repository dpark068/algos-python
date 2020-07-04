"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Algorithm:
1) If both LL are not None, add the two values and iterate to next
2) if the val is > 9, set a carry flag and append value - 10
3) If the size of LL's are uneven, will account for additional nums by checking each
4) Check for carry at end

Result:
Runtime: 68 ms, faster than 87.56% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.9 MB, less than 36.01% of Python3 online submissions for Add Two Numbers.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 and not l2:
            return None
        
        sumLL = sumCurr = ListNode(0)
        carry = False
        while l1 and l2:    # add both Linked List as long as both exist
                
            tempSum = l1.val + l2.val
            if carry:
                tempSum += 1
                carry = False
            
            if tempSum > 9:
                carry = True
                tempSum -= 10
            
            sumCurr.next = ListNode(tempSum)
            sumCurr = sumCurr.next
            l1 = l1.next
            l2 = l2.next
        
        
        # add remaining for each Linked List
        while l1 is not None:
            val = l1.val
            if carry:
                val += 1
                carry = False
            
            if val > 9:
                carry = True
                val -= 10
            sumCurr.next = ListNode(val)
            sumCurr = sumCurr.next
            l1 = l1.next
            
        while l2 is not None:
            val = l2.val
            if carry:
                val += 1
                carry = False
            
            if val > 9:
                carry = True
                val -= 10
            sumCurr.next = ListNode(val)
            sumCurr = sumCurr.next
            l2 = l2.next
        
        # Check for carry at end
        if carry:
            sumCurr.next = ListNode(1)
            sumCurr = sumCurr.next
            carry = False
            
        return sumLL.next
            
            
            