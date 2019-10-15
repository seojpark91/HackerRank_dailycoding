# LeetCode - Add Two Numbers (Medium)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummyHead = ListNode(0)
    curr = dummyHead
    carry = 0

    p = l1
    q = l2

    while p or q :
        x = p.val if p else 0
        y = q.val if q else 0
        summed_value = x + y + carry

        carry, out = divmod(summed_value, 10)

        curr.next = ListNode(out)
        curr = curr.next

        p = p.next if p else None
        q = q.next if q else None

    if carry > 0:
        curr.next = ListNode(carry)

    return dummyHead.next
