class LinkedList:

    # creates a singly linked list with only one Node and sets the pointer to None
    def __init__(self):
        self.head = None

    # inserts a new Node at the end of the list
    def insert(self, data):
        if self.get_head() == None:
            self.head = Node(data, None)
        else:
            current_node = self.get_head()
            while(current_node.next != None):
                current_node = current_node.next
            current_node.next = Node(data, None)

    def get_head(self):
        return self.head

    def print_all(self):
        print("printing all:")
        current_node = self.get_head()
        while (current_node):
            # format like this 1->2->3
            end_str = "->" if current_node.next else "\n"
            print(current_node.data, end=end_str)
            current_node = current_node.next


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


linked_list1 = LinkedList()
linked_list1.insert(1)
print(linked_list1.get_head().data)
linked_list1.insert(2)
linked_list1.insert(3)
linked_list1.print_all()
