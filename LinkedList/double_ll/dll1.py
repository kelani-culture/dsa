class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # creation of doubly linked list
    def createDLL(self, value):
        node = Node(value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLl CREATED SUCCESSFULLY"
    
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.createDLL(value)

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


doubly = DoublyLinkedList()
doubly.createDLL(5)
doubly.prepend(6)
doubly.prepend(2)
print(doubly.tail.value)
print([node.value for node in doubly])