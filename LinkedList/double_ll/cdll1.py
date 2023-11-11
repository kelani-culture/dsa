class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

        
        
# class CircularDoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
        
    
#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node = node
#             if node == self.tail.next:
#                 break

#     def CreateCdll(self, value):
#         node = Node(value)
#         self.head = node
#         self.tail = node
#         self.head.next = node
#         self.prev = node

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.CreateCdll(value)

#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#             self.head.prev = self.tail
#             self.tail.next = self.head
#             self.tail.prev = self.head

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break

    def CreateCdll(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.next = node
        self.prev = node
        # self.head.next = node
        # self.head.prev = node
        # self.tail.next = node
        # self.tail.prev = node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.CreateCdll(value)
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
            #self.tail.prev = self.head

cdll = CircularDoublyLinkedList()
cdll.prepend(1)
cdll.prepend(2)
cdll.prepend(3)
print(cdll.head.value)
print([node.value for node in cdll])