# create an single linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        # add to end of a node
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def add_to_beginning_node(self, value):
        # add to beginning of a node
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.tail.next = self.head
            self.head = self.tail
        self.length +=1

    def insert_at_idx(self, value, idx):
        new_node = Node(value)
        
        if idx < 0 and idx > self.length:
            return -1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(idx-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def __str__(self):
        # print element of a linked list
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '-->'
            temp_node = temp_node.next
        return result

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.add_to_beginning_node(5)

list1 = LinkedList()
list1.add_to_beginning_node(1)
list1.add_to_beginning_node(2)
list1.add_to_beginning_node(3)
list1.insert_at_idx(4, 0)
print(list1)
