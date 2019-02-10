def deleteNode(head, position):
    if position == 0:
        head = head.next
        return head
    
    else:
        cur = head
        for _ in range(position):
            prev = cur
            cur = cur.next
    prev.next = cur.next

    return head