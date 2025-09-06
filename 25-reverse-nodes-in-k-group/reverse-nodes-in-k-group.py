# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(s,e):
           p=None
           c=s
           while p!=e:  
            nn=c.next
            c.next=p
            p=c
            c=nn
           return e,s
        dummy=ListNode(0)
        dummy.next=head
        grp_p=dummy
        while True:
            kth=grp_p
            c=0
            while c<k and kth.next:
                kth=kth.next
                c+=1
            if c<k:
                break
            grp_nxt=kth.next
            nh,nt=reverse(grp_p.next,kth)
            grp_p.next=nh
            nt.next=grp_nxt
            grp_p=nt
            if grp_nxt is None:
                break
        return dummy.next