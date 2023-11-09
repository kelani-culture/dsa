"""
creating and working with doubly linked list
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
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
        self.length += 1
    
    
    def prepend(self, value):
        # add a node to the beginning of a linked list
        new_node = Node(value)
        if self.head is None:
            self.createDLL(value)

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1
            
    def append(self, value):
        # addd a node to the ending of a linked list
        new_node = Node(value)
        if self.head is None:
            self.createDLL(value)
        
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
    def insert(self, value, index):
       # insert at any given location 
        if index > self.length:
            print("Index out of range")
            exit()

        new_node = Node(value)
        if index == 0:
            self.prepend(value)
        
        elif index == self.length - 1:
            self.append(value)
        
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            new_node.next = temp
            new_node.prev = temp.prev
            temp.prev.next = new_node
            temp.prev = new_node
        self.length += 1
    
    def traverse(self):
        if self.head is None:
            print ("linked list is empty")
            exit() 

        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            
    def reverse_traverse(self):
        if self.head is None:
            print("linked list is empty")
            exit()
        
        temp = self.tail
        index = self.length
        while temp:
            index -= 1
            print(f"{index }: {temp.value}")
            temp = temp.prev

doubly = DoublyLinkedList()
doubly.createDLL(5)
doubly.prepend(6)
doubly.prepend(2)
doubly.append(3)
doubly.insert(1, 1)
doubly.reverse_traverse()
print([node.value for node in doubly])