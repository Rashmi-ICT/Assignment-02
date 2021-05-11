class Node:  # Create a class named as Node


    def __init__(self):  # define the object
        self.data = None  # define the attributes
        self.nref = None
        self.pref = None

    def setData(self, data):  # insert or set the instance values or data
        self.data = data

    def getData(self):  # get the data of the node
        return self.data

    def setNext(self, address):  # set next data  of the node
        self.nref = address

    def getNext(self):  # get next data  of the node
        return self.nref

    def setPrevious(self, address):  # set previous address  of the node
        self.pref = address

    def getPrevious(self):  # get previous data  of the node
        return self.pref
