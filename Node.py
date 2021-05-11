class Node: # Create a class named as Node
    def __init__(self): # define the object
        self.data = None # define the attributes
        self.nref = None
        self.pref = None

    def setData(self,data): # insert or set the instance values or data
        self.data = data

    def getData(self): #get the data
        return self.data

    def setNext(self,address): #set next data
        self.nref = address

    def getNext(self): # get next data
        return self.nref

    def setPrevious(self,address): # set previous address
        self.pref = address

    def getPrevious(self): # get previous data
        return self.pref
