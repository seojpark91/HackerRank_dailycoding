# Data Structure - Linked List series
def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        return new_node
    
    else:
        cur = head
        for _ in range(position):
            prev = cur
            cur = cur.next
        
        prev.next = new_node
        new_node.next = cur

        return head