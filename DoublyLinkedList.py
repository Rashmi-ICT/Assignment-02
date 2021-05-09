from Node import Node


class DoublyLinkedList: # create a new class  DoublyLinkedList
    def __init__(self): # then create a constructor
        self.head = Node() # creat a head and put on node
        self.head = None
        self.len = 0

    def print_LL(self):
        if self.head is None:  # ccffjdgjb
            print("linked list is empty")

        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=' ')
                n = n.nref

    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("Linked list is empty")

        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.pref

    # insert empty linked list

    def insert_empty(self, data):  # we create insert empty link list and take parameter self and data
        if self.head is None:  # firstly we check list empty or not
            new_node = Node(
                data)  # if it is none then create new node and we create a node using node class and pass the data
            self.head = new_node  # after creating node we point to new node
            self.len += 1

        else:
            print("lined list is not empty")  # link list is not empty, print a massage

    # add the begining linked list

    def add_begin(self, data):
        new_node = Node()  # create a new node pass the data parameter
        new_node.setData(data) # pass the data
        if self.head is None:   # we check head is none
            self.head = new_node #  after creating a node  we need to point to new node
        else:
            new_node.nref = self.head  #
            self.head.pref = new_node
            self.head = new_node
        self.len += 1

    def add_end(self, data):
        new_node = Node()
        new_node.setData(data)
        if self.head is None:
            self.head = new_node

        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.setNext(new_node)
            new_node.setPrevious(n)
        self.len += 1

    def remove_begin(self):
        if self.head is None:
            return None
        else:
            next = self.head.nref
            self.head = next
            next.setPrevious(None)
        self.len -= 1

    def remove_end(self):
        if self.head is None:
            return None
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n = n.pref
            n.setNext(None)
        self.len -= 1

    def add_nodePosition(self, pos, data):
        new = Node()
        new.setData(data)
        if pos < 0 or pos > self.len - 1:
            return None
        elif pos == 0:
            self.add_begin(data)
        elif pos == self.len - 1:
            self.add_end(data)
        else:
            count = 0
            n = self.head
            while count != pos:
                n = n.nref
                count += 1
            x = n.nref
            n.setNext(new)
            new.pref = n
            new.nref = x
            x.pref = new
            self.len += 1

    def remove_nodePosition(self, pos):
        if pos < 0 or pos > self.len - 1:
            return None
        elif pos == 0:
            self.remove_begin()
        elif pos == self.len - 1:
            self.remove_end()
        else:
            count = 0
            n = self.head
            while count != pos:
                n = n.nref
                count += 1
            x = n.pref
            y = n.nref
            x.setNext(y)
            y.setPrevious(x)
            self.len -= 1

    def search_given(self, pos):
        if pos < 0 or pos > self.len - 1:
            return None
        elif pos == 0:
            return self.head.data
        elif pos == self.len - 1:
            n = self.head
            while n.nref is not None:
                n = n.nref
            return n.data
        else:
            count = 0
            n = self.head
            while count != pos:
                n = n.nref
                count += 1
            return n.data

    def Dobly_Length(self): # create a new function for the doubly length
        n = self.head # start head
        count = 0
        while n is not None: #
            count += 1
            n = n.nref
        return count
