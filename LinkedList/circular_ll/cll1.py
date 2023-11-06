"""
performing operations in circular linked list
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

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

    def insert(self, value, idx=0):
        if idx > self.length:
            raise IndexError("Index out of range")
        new_node = Node(value)
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
        self.length += 1

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            
    def search(self, value):
        if self.head is  None:
            return None
        
        if self.head.value == value:
            return True

        current = self.head
        while current is not None:
            if current.value == value:
                return True

            current = current.next
            if current == self.head:
                break
        return False
    
    def get(self, idx):
        """
        get element in a linked list
        """
        if idx < -1 or idx > self.length:
            return -1
        if self.head is None:
            return None
        
        current = self.head
        for _ in range(idx):
            current = current.next
        return current
    
    def set():
        pass
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
csl.insert(2, 0)
csl.insert(3)
print(csl)
#print(csl.search(5))
print(csl.get(2))
