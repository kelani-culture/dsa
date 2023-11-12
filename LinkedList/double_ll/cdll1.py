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
        self.lenght += 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.CreateCdll(value)
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length += 1

    def insert(self, value, index):        
        if index < 0 or index > self.length:
            print("Index out of range")
            return
        
        
        new_node = Node(value)
        if index == 0:
            if self.head is None:
                self.CreateCdll(value)
            else:
                self.prepend(value)

        if index == self.length:
            self.append(value)
            
        else:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            new_node.next = temp_node
            new_node.prev = temp_node.prev
            temp_node.prev.next = new_node
            temp_node.prev = new_node

cdll = CircularDoublyLinkedList()
# cdll.prepend(1)
# cdll.prepend(3)
# cdll.prepend(4)
cdll.append(2)
cdll.append(3)
cdll.append(4)
cdll.insert(5, 3)
print([node.value for node in cdll])
