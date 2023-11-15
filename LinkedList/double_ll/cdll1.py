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
            
    def traversal(self):
        curr = self.head
        while curr:
            print(curr.value) 
            curr =  curr.next
            if curr is self.head:
                break

    def search(self, val):
        if self.head is None:
            return None
        
        elif self.head.next is None:
            return self
        temp = self.head
        while(temp):
            if temp.value == val:
                return True
            temp = temp.next
            if temp == self.head:
                break;
        return False
    
    def delete_node(self, index):
        if self.head is None:
            return None
        
        if index == 0:
            if self.length == 1:
                self.head.next = None
                self.head.prev = Noe
                self.head = None
                self.tail = None
            else:
                popNode = self.head
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
                popNode.next = None
                popNode.prev = None
                return popNode.value

        elif index == self.length - 1:
            popNode = self.tail
            self.tail = self.tail.prev
            self.tail.next = self.head
            popNode.next = None
            popNode.prev = None
            return popNode.value
        
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next

            popNode = temp
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            popNode.next = None
            popNode.prev = None
            return popNode
            
cdll = CircularDoublyLinkedList()
# cdll.prepend(1)
# cdll.prepend(3)
# cdll.prepend(4)
cdll.append(2)
cdll.append(3)
cdll.append(4)
cdll.insert(5, 3)
# cdll.traversal()
print([node.value for node in cdll])
cdll.delete_node(1)
print([node.value for node in cdll])
#print(cdll.search(2))
