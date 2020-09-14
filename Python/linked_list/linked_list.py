
# a linked list is a data structure that has its benefits over an array in that adding and deleting elements can be done in O(1) time
# however one disadvantage of a linked list over an array is that searching for a random element takes O(n) time
# verdict: use a linked list whenever you know ahead of compilation that you need a data structure that will have more adding/deletions than searches


class LinkedList:

    # creates an empty singly linked list
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

        if (current_node.data == data):
            temp = current_node
            self._head = current_node.next
            del temp
            return

        while (current_node.next):
            if (current_node.next.data == data):
                if (current_node.next == self.get_tail()):
                    current_node.next = None
                    self._tail = current_node
                    return
                else:
                    current_node.next = current_node.next.next
                    return

            else:
                current_node = current_node.next

    # deletes only the first occurence of reference
    def delete_by_reference(self, pointer):
        current_node = self.get_head()

        if (current_node == pointer):
            temp = current_node
            self._head = current_node.next
            del temp
            return

        while (current_node.next):
            if (current_node.next == pointer):
                if (current_node.next == self.get_tail()):
                    current_node.next = None
                    self._tail = current_node
                else:
                    current_node.next = current_node.next.next


            else:
                current_node = current_node.next

    # deletes all occurences of data
    def delete_all(self, data):
        current_node = self.get_head()

        if (current_node.data == data):
            temp = current_node
            self._head = current_node.next
            del temp

        while (current_node.next):
            if (current_node.next.data == data):
                if (current_node.next == self.get_tail()):
                    current_node.next = None
                    self._tail = current_node
                else:
                    current_node.next = current_node.next.nex

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
    
    def remove_dups(self):
        current_node = self.get_head()

        while (current_node):
            target_data = current_node.data
            search_node = current_node.next
            while(search_node):
                if(search_node.data == target_data):
                    self.delete_by_reference(search_node)
                    search_node = search_node.next
                else:
                    search_node = search_node.next
            current_node = current_node.next



    def delete_tail(self):
        tail = self.get_tail()
        current_node = self.get_head()
        while (current_node):
            if (current_node.next == tail):
                current_node.next = None
                self._tail = current_node
                return
                
            current_node = current_node.next


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    # todo: create an edit method on a given node

    def edit(self, target_data):
        self.data = target_data


linked_list1 = LinkedList()
# create a linked list with 20 nodes each one a duplicate
for i in range(0, 3):
    linked_list1.insert(i)
    linked_list1.insert(i)

linked_list1.remove_dups()

linked_list1.print_all()