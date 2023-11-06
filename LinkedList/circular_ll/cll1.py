"""
performing operations in circular linked list
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
 
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self, value, idx):
        new_node = Node(value)
        
        if idx >= self.length:
            return -1
        if idx == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
    
        elif self.length - 1 == idx:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        
        else:
            temp_node = self.head
            for _ in range(idx -1):
                temp_node = temp_node.next
                
            new_node.next = temp_node.next
            temp_node.next = new_node

    def __str__(self):
        circle = self.head
        res = ""
        while circle:
            res += str(circle.value)
            circle = circle.next
            if circle is self.head:
                break
            res += '--->'
        return res
    

csl = CSLinkedList()
csl.prepend(10)
csl.prepend(5)
csl.prepend(3)
csl.prepend(1)
csl.insert(2, 3)
print(csl)