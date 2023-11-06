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
csl.append(10)
csl.append(5)
csl.append(3)
csl.append(1)
print(csl)