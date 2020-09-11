
# a linked list is a data structure that has its benefits over an array in that adding and deleting elements can be done in O(1) time
# however one disadvantage of a linked list over an array is that searching for a random element takes O(n) time
# verdict: use a linked list whenever you know ahead of compilation that you need a data structure that will have more adding/deletions than searches


class LinkedList:

    # creates a singly linked list with only one Node and sets the pointer to None
    def __init__(self):
        self._head = None
        self._tail = None

    # inserts a new Node at the end of the list
    def insert(self, data):
        if self.get_head() == None:
            self._head = Node(data, None)
            self._tail = self._head
        else:
            new_node = Node(data, None)
            self._tail.next = new_node
            self._tail = new_node

    # deletes only the first occurence of data
    def delete(self, data):
        current_node = self.get_head()
        while (current_node.next):
            if (current_node.next.data == data):
                temp = current_node.next
                current_node.next = current_node.next.next
                del temp
                return

            else:
                current_node = current_node.next

                

    # deletes all occurences of data
    def delete_all(self, data):
        current_node = self.get_head()
        while (current_node.next):
            if (current_node.next.data == data):
                temp = current_node.next
                current_node.next = current_node.next.next
                del temp
            else:
                current_node = current_node.next

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

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

    def edit_node(self, data, target_data):
        current_node = self.get_head()
        while (current_node):
            if (current_node.data == data):
                current_node.edit(target_data)
                return
            current_node = current_node.next
        if (not current_node):
            print("node not found")

    def runner_search(self, data):
        single_step_p = self.get_head()
        double_step_p = self.get_head()
        while (single_step_p):
            if (single_step_p.data == data):
                return single_step_p
            else:
                single_step_p = single_step_p.next
            if (double_step_p.data == data):
                return double_step_p
            elif (double_step_p.next.next):
                double_step_p = double_step_p.next.next
        return None

    def delete_list(self):
        # use the runner method to delete all node in the list, even though in python that's not necessary but for the sake of problem solving skills
        single_step_p = self.get_head()
        while (single_step_p != self._tail):
            temp = single_step_p
            single_step_p = single_step_p.next
            del temp
        del self._tail
        self._head = None
        self._tail = None
        


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    # todo: create an edit method on a given node

    def edit(self, target_data):
        self.data = target_data


linked_list1 = LinkedList()
# linked_list1.insert(1)
# linked_list1.insert(2)
# linked_list1.insert(3)
# print(linked_list1.get_head().data)
# linked_list1.insert(4)
# linked_list1.insert(3)
# linked_list1.insert(3)
# linked_list1.print_all()
# linked_list1.delete(3)
# linked_list1.print_all()
# linked_list1.delete_all(3)
# linked_list1.print_all()
# linked_list1.edit_node(4, 40)
# linked_list1.print_all()
# linked_list1.edit_node(41, 5)
# linked_list1.print_all()
for i in range(0, 20):
    linked_list1.insert(i)
linked_list1.print_all()

for i in range(0, 20):
    print(linked_list1.runner_search(i).data)
linked_list1.delete_list()
linked_list1.print_all()
