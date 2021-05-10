from Node import Node


class DoublyLinkedList:  # create a new class  DoublyLinkedList
    def __init__(self):  # then create a constructor
        self.head = Node()  # creat a head and put on node
        self.head = None  # define head as none
        self.len = 0  # define DoublyLinkedList length as 0

    def print_LL(self):  # method to foreword printing
        if self.head is None:  # check head is none or not
            print("linked list is empty")  # if head = none, print a massage

        else:  # then create a variable as n and assign  head  to it
            n = self.head
            while n is not None:  # while n is not none print the value of n and get next value of the DoublyLinkedList in to n
                print(n.data, "-->", end=' ')
                n = n.nref  # when n is none loop will stop

    def print_LL_reverse(self):  # method to backward printing
        print()
        if self.head is None:  # check head is none or not
            print("Linked list is empty")  # if head = none, print a massage

        else:
            n = self.head  # create a variable and assign  head to it.
            while n.nref is not None:  # get the next value of the n and run loop until next value of the n is not none to get next of the n
                n = n.nref
            while n is not None:  # whlie n is not none print the value n and get the previous value of the n in to variable n
                print(n.data, "-->", end=" ")
                n = n.pref

    # insert empty linked list

    def insert_empty(self, data):  # we create insert empty link list and take parameter self and data
        if self.head is None:  # firstly we check list empty or not
            new_node = Node(
                data)  # if it is none then create new node and we create a node using node class and pass the data
            self.head = new_node  # after creating node we point to new node
            self.len += 1  # increas length by 1

        else:
            print("lined list is not empty")  # link list is not empty, print a massage

    # add the begining linked list

    def add_begin(self, data):
        new_node = Node()  # create a new node pass the data parameter
        new_node.setData(data)  # pass the data
        if self.head is None:  # we check head is none
            self.head = new_node  # after creating a node  we need to point to new node
        else:
            new_node.nref = self.head  # define  the next of the created  new node is to  current head
            self.head.pref = new_node  # previous of the current head is new node
            self.head = new_node  # current head is new node
        self.len += 1  # increas length by 1

    # add the  end linked list

    def add_end(self, data):
        new_node = Node()  # create a new node pass the data parameter
        new_node.setData(data)  # pass the data
        if self.head is None:  # we check head is none
            self.head = new_node  # after creating a node  we need to point to new node

        else:
            n = self.head  # create a variable and assign  head to it.
            while n.nref is not None:  # get the next value of the n and run loop until next value of the n is not none to get next of the n
                n = n.nref
            n.setNext(new_node)  # then n is none set the next of the end  is new node
            new_node.setPrevious(n)  # set n as the previous of ne node
        self.len += 1  # increase length by 1

    # remove the  begging linked list

    def remove_begin(self):  # create a method to remove the head
        if self.head is None:  # check head is none or not
            return None  # if head = none return none
        else:
            next = self.head.nref  # create a varible as next and next value of the head assign to it.
            self.head = next  # define the head
            next.setPrevious(None)  # previous of the head set as  none
        self.len -= 1  # decrease length by 1

    # remove the  end  linked list

    def remove_end(self):  # create a method to remove the end
        if self.head is None:  # check head is none or not
            return None  # if head = none return none
        else:
            n = self.head  # create a variable and assign  head to it.
            while n.nref is not None:  # get the next value of the n and run loop until next value of the n is not none to get next of the n
                n = n.nref
            n = n.pref  # get the previous value of end
            n.setNext(None)  # set the next of the end as none
        self.len -= 1  # decrease length by 1

    # add the possitional node

    def add_nodePosition(self, pos, data):  # create a method and pass the position and data
        new = Node()  # create a new node and set the data
        new.setData(data)
        if pos < 0 or pos > self.len - 1:  # set the given position is less than 0 or grater than length -  1
            return None  # then if it is return none
        elif pos == 0:  # checked  the position == 0
            self.add_begin(data)  # call the method add_begin(data)
        elif pos == self.len - 1:  # checked given position self len -1
            self.add_end(data)  # then call the method add_end(data)
        else:
            count = 0  # create a variable and set it value as 0
            n = self.head  # create a variable and assign  head in to it
            while count != pos:  # run loop until count != position
                n = n.nref  # get the next of the n in to n
                count += 1  # increase length by 1
            x = n.nref  # get the next of the end in to variable x
            n.setNext(new)  # set the new node  as the next of the n
            new.pref = n  # set the n as the previous of the new
            new.nref = x  # set the x as the next of the new
            x.pref = new  # set the new as the previous of x
            self.len += 1  # increase length by 1

    # remove the positional node

    def remove_nodePosition(self, pos):  # create a method and pass the position
        if pos < 0 or pos > self.len - 1:  # checked the given position is less than  or 0 or grater than length - 1
            return None  # if it is return none
        elif pos == 0:  # if pos == 0 , then call the method remove_begin()
            self.remove_begin()
        elif pos == self.len - 1:  # if position = length - 1 ,then call the method remove remove_end()
            self.remove_end()
        else:
            count = 0  # create a variable and set it value as 0
            n = self.head  # create a variable and assign  head in to it
            while count != pos:  # run loop until count != position
                n = n.nref  # get the next of the n in to n
                count += 1  # increase length by 1
            x = n.pref  # create variable x and set the value of x is previous  of the n
            y = n.nref  # create a variable y and set the value of the y is next of the end
            x.setNext(y)  # set the next of the x is y
            y.setPrevious(x)  # set the previous of the y  is x
            self.len -= 1  # # decrease length by 1

    # create  search_given

    def search_given(self, pos):  # create a method and pass the position
        if pos < 0 or pos > self.len - 1:  # checked the given position is less than  or 0 or grater than length - 1
            return None  # if it is return none
        elif pos == 0:  # # if pos == 0 , then return data of the the head
            return self.head.data
        elif pos == self.len - 1:  # if position = length - 1 ,then assign head to variable n
            n = self.head
            while n.nref is not None:  # run loop until next of the n is not non , get  next of n in to variable n
                n = n.nref
            return n.data  # when next of the n is none return data of the n
        else:
            count = 0  # create a variable and set it value as 0
            n = self.head  # create a variable and assign  head in to it
            while count != pos:  # run loop until count != position
                n = n.nref  # get the next of the n in to n
                count += 1  # increase count by 1
            return n.data  #  return  the data of the n

    def Dobly_Length(self):  # create a new function for the doubly length
        n = self.head  # create a variable n and assign the head
        count = 0  # create a variable and set it value as 0
        while n is not None:  # run loop until n is not none
            count += 1  # increase count by 1
            n = n.nref  # get the next of the n in to n
        return count # return the count
