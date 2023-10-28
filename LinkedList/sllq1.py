# a code that implement a singly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def delete_node(self, index):
        if self.head is None:
            return None
        
        if index < 0 or index >= self.length:
            return None

        if index == 0:

            if self.length == 1:
                self.head = self.tail = None
            temp = self.head
            self.head = self.head.next
            temp = temp.next = None
            return temp

        else:
            prev_node = self.head
            for _ in range(index-1):
                prev_node = prev_node.next
           
            temp = prev_node.next
            prev_node.next = prev_node.next.next
            temp.next = None
        return temp

    def reverse(self):
        prev = None
        current = self.head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            print(current.next.value)
            prev =  current
            current = next_node
        self.head = prev

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
print(ll)
ll.reverse()
print(ll)
#ll.delete_node(1)
#print(ll)
