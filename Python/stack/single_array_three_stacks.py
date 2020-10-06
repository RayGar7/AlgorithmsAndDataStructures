class FixedMultiStack:
    def __init__(self, size):
        if (size % 3 != 0):
            raise Exception("size must be divisible by 3")

        self.array = [None] * size

        self.stack_tops = [
            0,
            int(size / 3),
            int(2 * size / 3)
        ]

    def get_array_size(self):
        return len(self.array)

    # data is the data to pass and stack is the stack - 1 to choose from the 3 stacks (0-based)
    def push(self, data, stack):
        relative_index = stack-1

        # is given stack is full
        if (self.stack_tops[relative_index] == self.get_array_size() * stack / 3):
            raise Exception("Given stack is full")
        else:
            absolute_index = self.stack_tops[relative_index]
            self.array[absolute_index] = data
            self.stack_tops[stack-1] += 1


    def pop(self, stack):
        relative_index = stack-1
        absolute_index = self.stack_tops[relative_index]-1
        if (self.stack_tops[relative_index] in [0, int(self.get_array_size() / 3), int(2 * self.get_array_size() / 3)]):
            raise Exception("Given stack is empty")

        temp = self.array[absolute_index]
        self.array[absolute_index] = None
        self.stack_tops[relative_index] -= 1
        return temp

    # runs in O(n)
    def empty(self):
        for e in self.array:
            if (e != None):
                return False

        return True

    def peek_at_stack(self, stack):
        relative_index = stack-1
        absolute_index = self.stack_tops[relative_index]-1
        return self.array[absolute_index]


    def peek_all(self):
        pass




stack1 = FixedMultiStack(6)
stack1.push(1, 1)
stack1.push(2, 2)
stack1.push(3, 3)
print(stack1.array)
stack1.pop(1)
print(stack1.array)
stack1.pop(2)
print(stack1.array)
stack1.pop(3)
print(stack1.array)
stack1.push(1, 1)
stack1.push(2, 2)
stack1.push(3, 3)
print(stack1.array)
print(stack1.peek_at_stack(3))