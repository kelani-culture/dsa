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
        # traverse the list in reverse order
        if self.head is None:
            print("linked list is empty")
            exit()
 
        temp = self.tail
        index = self.length
        while temp:
            index -= 1
            print(f"{index }: {temp.value}")
            temp = temp.prev
            
        
    def search(self, value):
        if self.head is None:
            return None
        
        temp = self.head
        while temp:
            if temp.value == value:
                return temp.value
            temp= temp.next
            
        return "Node does not exist"
    
    def popFirst(self):
        # delete first value in a doubly linked list
        if self.head is None:
            return None

        pophead = self.head
        if self.head.next is None:
            self.head = None
            self.tail = None
        
        else:
            self.head = self.head.next
            self.head.prev = None 
        self.length -= 1
        return pophead.value
    
    def pop(self):
        if self.head is None:
            print("linked list is empty")
            exit()

        poplast = self.tail
        if self.head.next is None:
            self.head = None
            self.tail = None 
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            
        self.length -= 1
        return poplast.value

    def remove_node(self, index):
        if self.head is None:
            print("empty linked list")
            exit()

        if index == 0:
          return self.popFirst()

        elif index == self.length - 1:
            return self.pop()
            
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
        self.length -= 1
        return temp.value

    
    def delete_all(self):
        if self.head is None:
            print("empty linked list")
            exit()
       
        temp = self.head
        while temp:
            temp.prev = None
            temp =  temp.next
            
        self.head = None
        self.tail = None

doubly = DoublyLinkedList()
doubly.createDLL(5)
doubly.prepend(6)
doubly.prepend(2)
doubly.append(3)
doubly.insert(1, 1)
# doubly.reverse_traverse()

print([node.value for node in doubly])
print(doubly.popFirst())
print([node.value for node in doubly])
print(doubly.remove_node(3))
print([node.value for node in doubly])
print(doubly.pop())
print([node.value for node in doubly])
print(doubly.delete_all())
print([node.value for node in doubly])

