# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head node to simplify list construction
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop until both lists are empty and there is no remaining carry
        while l1 or l2 or carry:
            # Extract values from current nodes, default to 0 if list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for this position
            total = val1 + val2 + carry
            
            # Update carry and calculate new digit value
            carry = total // 10
            new_digit = total % 10
            
            # Append new node to the result list
            current.next = ListNode(new_digit)
            current = current.next
            
            # Move to next nodes in input lists if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy_head.next
