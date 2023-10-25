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
        # insert at a specific index
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

    def traverse(self):
        """
            traverse a list
        """
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search_node(self, value):
        """
            check if a value exist in the list
            and return true if its exist
            else false
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def search_node_idx(self, value):
        """
            search a node by value and return the index
            else return -1
        """
        current = self.head
        idx = 0
        while current:
            if current.value == value:
                return idx
            idx += 1
            current = current.next
        return -1
    
    def get(self, index):
        """
            takes an index and return
            the address at the index
        """
        current = self.head
        if index < -1 or index >= self.length:
            return None

        if index == -1:
            # return last node
            return self.tail
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        # update the value at a given index
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def popFirst(self):
        # delete the first element in the node
        # and returns the element
        if self.head is None:
            return None
        current = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            current.next = None
            self.length -= 1
        return current.value
    
    def popLast(self):
        popped_node = self.tail

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.add_to_beginning_node(5)

list1 = LinkedList()
#list1.add_to_beginning_node(1)
#list1.add_to_beginning_node(2)
list1.add_to_beginning_node(3)
#list1.insert_at_idx(4, 0)
#print(list1)
#list1.traverse()
#print(list1.search_node_idx(4))
# get node
#print(list1.get(-1).value)
#print(list1)
list1.set_value(0, 5)
#print(list1)
print(list1.popFirst())
print(list1.tail.value)
