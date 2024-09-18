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
            temp_node = new_node
            temp_node.next = self.head
            self.head = temp_node
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
        # pop last element in a linked list
        if self.head is None:
            return None
        
        if self.head == 1:
            self.head = self.tail = None

        else:
            temp_node = self.head
            popped_node = self.tail
            while temp_node.next is not self.tail:
                temp_node = temp_node.next

            self.tail = temp_node
            temp_node = None
            self.length -= 1
            return popped_node.value

    def remove_node(self, index):
        if self.head is None:
            return None

        if index < 0 or index >= self.length:
            return None
        # check if node is a single element
        if self.length == 1:
            self.head = None
            self.tail = None
        # check if index is at the beginning
        if index == 0:
            removed = self.head
            self.head = self.head.next
            removed = None
        # check if index is at end
        elif index == self.length - 1:
            removed_node = self.tail
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
            removed_node = None
        # check if index is inbetween
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            removed_node = temp.next
            temp.next = temp.next.next
            removed_node = None
        self.length -= 1

    def delete(self):
        # delete everyting in a linked list
        self.head = None
        self.tail = None
        self.length = 0

new_linked_list = LinkedList()
#new_linked_list.append(10)
#new_linked_list.append(20)
#new_linked_list.append(30)
#new_linked_list.append(40)
new_linked_list.append(60)
print(new_linked_list)
new_linked_list.delete()
print(new_linked_list)
