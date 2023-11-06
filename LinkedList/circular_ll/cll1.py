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
            return None
        if self.head is None:
            return None
        
        current = self.head
        for _ in range(idx):
            current = current.next
        return current
    
    def set(self, index, value):
        # update a value in a linked list
        if self.head is None:
            return None
        
        node = self.get(index)
        if node:
            node.value = value
        return self.head
    
    def popFirst(self):
        if self.head is None:
            return None
        
        pop_head = self.head
        if self.head.next is self.head:
            self.head.next = None
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.tail.next = self.head
            pop_head.next = None
        self.length -= 1
        return pop_head
    
    def popLast(self):
        if self.head is None:
            return None
        pop_last = self.tail
        if self.head.next is self.head:
            self.head.next = None
            self.head = None
            self.tail = None
            
        else:
            prev = self.head
            while prev.next is not self.tail:
                prev = prev.next 
            self.tail = prev
            self.tail.next = self.head
            pop_last.next = None
        return pop_last
    
    def remove(self, idx):
        if self.head is None:
            return None
        
        if idx < 0 or idx >= self.length:
            return None
        if idx == 0:
            self.length -= 1
            return self.popFirst()
            
        elif idx == self.length -1:
            self.length -=1
            return self.popLast()
        else:
            prev = self.head
            for _ in range(idx-1):
                prev = prev.next
            temp = prev.next
            prev.next = prev.next.next
            #prev.next = None
            self.length -= 1
            return temp
 
    def delete(self):
        if self.head is None:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0

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
# print(csl.get(2))
# csl.set(5, 1000)
#print(csl.popFirst())
#csl.popLast()
#csl.remove(4)
csl.delete()
print(csl)
