# remove duplicates from linked list
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

    def remove(self, node):
        if node is None:
            return None

    def remove_duplicates(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            return self
        seen = set()
        curr = self.head
        prev = None
        while curr:
            if curr.value in seen:
                prev.next = curr.next
            else:
                seen.add(curr.value)
                prev = curr
            curr = curr.next
        return self.head
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(4)
ll.append(4)
ll.remove_duplicates()
print(ll)
