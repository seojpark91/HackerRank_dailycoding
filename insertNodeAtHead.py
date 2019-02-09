# Data Structures - Linked List
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def insertNodeAtHead(llist, data):
    new_node = SinglyLinkedListNode(data)
    if llist == None:
        llist = new_node
        return llist
    else:
        new_node.next = llist
        llist = new_node
        return llist