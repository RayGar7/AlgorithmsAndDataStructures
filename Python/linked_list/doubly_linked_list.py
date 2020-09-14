# a doubly linked list is a data structure that is just like a singly linked list but each node also has a pointer to the previous Node in the linked list
# verdict: use a doubly linked list whenever searching for an item in the linked list requires "backtracking"

class DoublyLinkedList:

    # creates a doubly linked list with only one Node and sets the pointer to None
    def __init__(self):
        self._head = None
        self._tail = None


    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    # inserts a new Node at the end of the list
    def insert(self, data):
        if self.get_head() == None:
            self._head = Node(data, None, None)
            self._tail = self._head
        else:
            # create a node whose previous pointer is set to the current tail
            # then set the current tail's next pointer to the new node
            # and set the new node as the new tail
            new_node = Node(data, None, self._tail)
            self._tail.next = new_node
            self._tail = new_node

    def print_all(self):
        if not self._head:
            print("the list is empty")
            return
        print("printing all:")
        current_node = self.get_head()
        while (current_node):
            # format like this 1->2->3
            end_str = "->" if current_node.next else "\n"
            print(current_node.data, end=end_str)
            current_node = current_node.next

    def print_all_backwards(self):
        if not self._head:
            print("the list is empty")
            return
        print("printing all:")
        current_node = self.get_tail()
        while (current_node):
            # format like this 1->2->3
            end_str = "->" if current_node.previous else "\n"
            print(current_node.data, end=end_str)
            current_node = current_node.previous



    # # deletes only the first occurence of data
    def delete(self, data):
        current_node = self.get_head()

        while (current_node):
            if (current_node.data == data and current_node.next != None and current_node.previous != None):
                current_node.next.previous = current_node.previous
                current_node.previous.next = current_node.next
                del current_node
                return
            # if at the tail
            elif (current_node.data == data and current_node.next == None):
                self._tail = current_node.previous
                current_node.previous.next = None
                del current_node
                return

            # if at the head
            elif (current_node.data == data and current_node.previous == None):
                self._head = current_node.next
                current_node.next.previous = None
                del current_node
                return
            else:
                current_node = current_node.next

        print("node not found")

                

    # # deletes all occurences of data
    def delete_all(self, data):
        current_node = self.get_head()
        while (current_node.next):
            if (current_node.next.data == data):
                temp = current_node.next
                current_node.next = current_node.next.next
                del temp
            else:
                current_node = current_node.next

    # def edit_node(self, data, target_data):
    #     current_node = self.get_head()
    #     while (current_node):
    #         if (current_node.data == data):
    #             current_node.edit(target_data)
    #             return
    #         current_node = current_node.next
    #     if (not current_node):
    #         print("node not found")

# todo: implment double step using inheritance
#    def runner_search(self, data):

    # def delete_list(self):
    #     del self
        


class Node:
    def __init__(self, data, next, previous):
        self.data = data
        self.next = next
        self.previous = previous

    def edit(self, target_data):
        self.data = target_data




linked_list1 = DoublyLinkedList()
for i in range(0, 20):
    linked_list1.insert(i)
linked_list1.delete(0)
linked_list1.delete(10)
linked_list1.delete(19)
linked_list1.delete(190)
linked_list1.print_all()
linked_list1.print_all_backwards()

# todo: create an abstract super class to base both the singly linked list and the doubly linked list to make both classes DRYer