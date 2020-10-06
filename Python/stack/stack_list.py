class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def peek_all(self):
        print(self.stack)

    def peek_last(self):
        return self.stack[len(self.stack) - 1]


'''
Uncomment the following lines to run a test run of the Stack class
'''
# stack1 = Stack()
# stack1.peek()

# stack1.push("L")
# stack1.push("R")
# stack1.push("L")
# stack1.push("L")
# stack1.push("R")
# stack1.push("R")
# stack1.push("L")
# stack1.push("R")
# stack1.peek()

# stack1.pop()
# stack1.pop()
# stack1.peek()