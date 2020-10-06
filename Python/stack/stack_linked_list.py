class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    class StackNode:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next


    def pop(self):
        if self._top == None:
            raise Exception("Cannot pop from an empty stacks")
        temp = self._top
        del self._top
        self._top = temp.next
        return temp.data     

    def push(self, data):
        new_node = self.StackNode(data, None)
        if (self.isEmpty()):
            self._top = new_node
        else:
            new_node.next = self._top
            self._top = new_node
        

    def peek(self):
        if self._top == None:
            raise Exception("Cannot peek from an empty stacks")
        return self._top.data

    def isEmpty(self):
        return self._top == None

stack1 = Stack()
stack1.push(1)
stack1.push(2)

for i in range(1,11):
    stack1.push(i)

for i in range(10):
    print(stack1.pop())


