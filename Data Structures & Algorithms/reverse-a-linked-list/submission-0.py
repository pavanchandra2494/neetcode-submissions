# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr,prev=head,None
        while curr:
            temp=curr.next #first maintaining the chain to move curr later one step forward
            curr.next=prev #pointing head/current element to its previous element
            prev=curr #moving prev one step forward
            curr=temp #moving current element one step forward
        return prev



        