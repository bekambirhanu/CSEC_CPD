# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummyNode = ListNode(0)
        tail = dummyNode

        while (l1 is not None) or (l2 is not None) or (carry !=0):
            count_l1= l1.val if l1 else 0
            count_l2= l2.val if l2 else 0

            total = count_l1 + count_l2 + carry
            carry = total // 10
            newNode = ListNode(total % 10)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        result = dummyNode.next
        return result