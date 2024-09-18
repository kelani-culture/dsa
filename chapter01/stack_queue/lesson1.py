# The stack data structures
# simple implementation of the stack data structure


class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(s) for s in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        return True if self.list == [] else False

    def push(self, value):
        self.list.append(value)
        return "value has been added"

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()
    def peek(self):
        if self.isEmpty():
            return "Empty stack"
        else:
            return self.list[len(self.list) - 1]
    def delete(self):
        self.list = None

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
#print(customStack.isEmpty())
#print('----------->',customStack.pop())
print(customStack.peek())
