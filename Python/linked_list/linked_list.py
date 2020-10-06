# a linked list is a data structure that has its benefits over an array in that adding and deleting elements can be done in O(1) time
# however one disadvantage of a linked list over an array is that searching for a random element takes O(n) time
# verdict: use a linked list whenever you know ahead of compilation that you need a data structure that will have more adding/deletions than searches

class LinkedList:
    # creates an empty singly linked list
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    # inserts a new Node at the end of the list
    def insert(self, data):
        if self.get_head() == None:
            self._head = Node(data, None)
            self._tail = self._head
        else:
            new_node = Node(data, None)
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

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
        self._size -= 1

    # deletes a node by reference
    def delete_by_reference(self, pointer):
        if (pointer == self.get_tail()):
            self.delete_tail()
            return

        current_node = self.get_head()

        if (current_node == pointer):
            temp = current_node
            self._head = current_node.next
            del temp
            return

        while (current_node.next):
            if (current_node.next == pointer):
                if (current_node.next != self.get_tail()):
                    current_node.next = current_node.next.next
                else:
                    current_node.next = None
                    self._tail = current_node

            else:
                current_node = current_node.next
        self._size -= 1

    # deletes all occurences of data
    def delete_all(self, data):
        delete_amount = 0
        current_node = self.get_head()

        if (current_node.data == data):
            temp = current_node
            self._head = current_node.next
            del temp
            delete_amount += 1

        while (current_node.next):
            if (current_node.next.data == data):
                if (current_node.next == self.get_tail()):
                    current_node.next = None
                    self._tail = current_node

                else:
                    current_node.next = current_node.next.next
                delete_amount += 1

            else:
                current_node = current_node.next
        
        self._size -= delete_amount

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
        # delete all of the nodes in the list, even though in python that's not necessary but for the sake of problem solving skills
        single_step_p = self.get_head()
        while (single_step_p != self._tail):
            temp = single_step_p
            single_step_p = single_step_p.next
            del temp
        del self._tail
        self._head = None
        self._tail = None
        self._size = 0
    
    def remove_dups(self):
        delete_amount = 0
        current_node = self.get_head()

        while (current_node):
            target_data = current_node.data
            search_node = current_node.next
            while(search_node):
                if(search_node.data == target_data):
                    self.delete_by_reference(search_node)
                    search_node = search_node.next
                    delete_amount += 1
                else:
                    search_node = search_node.next
            current_node = current_node.next
        self._size -= delete_amount


    def delete_tail(self):
        tail = self.get_tail()
        current_node = self.get_head()

        if (tail == current_node):
            self._head = None
            self._tail = None
            return
        while (current_node):
            if (current_node.next == tail):
                current_node.next = None
                self._tail = current_node
                self._size -= 1
                return
                
            current_node = current_node.next

    # returns the kth to the last node in the linked list
    # O(n+(n-k-1)) = O(2n-k-1)
    def kth_to_the_last(self, k):

        # similarily I could find the length inside this method (or create a helper) to get the size of the linked list
        size = self.get_size()

        steps = size - k
        current_node = self.get_head()
        for i in range(0, steps-1):
            current_node = current_node.next
        return current_node

    # returns the size of the linked list
    # runs in O(n) everytime where n is the number of nodes in the linked list
    def get_size(self):
        size = 0
        current_node = self.get_head()
        while(current_node):
            current_node = current_node.next
            size += 1
        return size

    # deletes a node from the middle of a linked list (not necessarily the exact middle but any node that is not the head or the tail)
    # you only have access to n, the node in the middle of the linked list
    def delete_from_middle(self, n):
        # raise an exception if n is the tail
        # however there is no way to check if n is the head
        if (n.next == None):
            raise Exception("Node is not in the middle of the linked list")
        temp_data = n.next.data
        n.data = temp_data
        n.next = n.next.next
        self._size -= 1

    # O(n^2) because we are moving i a total of N times, and for time we move i we also move shift up a total of (len-i) times
    def is_palindrome(self):

        temp_list = LinkedList()
        temp_p = self.get_head()
        while(temp_p):
            temp_list.insert(temp_p.data)
            temp_p = temp_p.next

        temp_head = temp_list.get_head()
        while (temp_head):
            if (temp_head.data == temp_list.get_tail().data):
                # repeat
                # delete the head and delete the tail
                temp_head = temp_head.next
                # todo need to test if it works on a tail node
                temp_list.delete_by_reference(temp_list.get_tail())
            else: 
                return False
        return True

    # there's a few different ways to implement this method depednign on what the instance needs to be
    # I can return a new instance and not edit the current one
    # I can also edit the data values (and not the references)
    # or I can create new references for the nodes (and not the linked list instance)
   # however for the sake of time, I'm just going to return a new linked list with the reversed values 
    # O(n*log(n))
    def reverse(self):
        reversed_list = LinkedList()
        temp_list = LinkedList()
        temp_p = self.get_head()
        # O(n)
        while(temp_p):
            temp_list.insert(temp_p.data)
            temp_p = temp_p.next

        # O(n*log(n))
        while(temp_list.get_head()):
            reversed_list.insert(temp_list.get_tail().data)
            temp_list.delete_tail()
        return reversed_list

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    # todo: create an edit method on a given node

    def edit(self, target_data):
        self.data = target_data


linked_list1 = LinkedList()

def partition(linked_list, partition):
    current_node = linked_list.get_head()
    linked_list_left = LinkedList()
    linked_list_right = LinkedList()

    while (current_node):
        if (current_node.data < partition):
            linked_list_left.insert(current_node.data)
        else:
            linked_list_right.insert(current_node.data)
        current_node = current_node.next
 
    # join the two linked lists
    linked_list_left._tail.next = linked_list_right._head
    linked_list_left._tail = linked_list_right._tail

    return linked_list_left


# todo: this does not take into account differently sized lists
def sum_lists(l1,l2):
    node_1 = l1._head
    node_2 = l2._head
    sum_list = LinkedList()

    travel_node = (node_1 if l1._size >= l2._size else node_2)
    carry = False

    while(travel_node):
        sum = node_1.data + node_2.data
        if (carry):
            sum += 1

        carry = sum >= 10
        sum_list.insert(sum % 10)
        node_1 = node_1.next
        node_2 = node_2.next
        travel_node = travel_node.next

    return sum_list
