"""
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.
The list is very long, so making more than one pass is prohibitively expensive.
Do this in constant space and in one pass.

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_kth_last(head: ListNode, k: int) -> ListNode:
    slow = fast = head
    for _ in range(k):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
