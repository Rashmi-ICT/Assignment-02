from DoublyLinkedList import DoublyLinkedList


print("==============================================================")
Doubly = DoublyLinkedList()
Doubly.print_LL()

print("==============================================================")
print("\nADD BEGINNING\n")

Doubly.add_begin(1000)
Doubly.add_begin(100)
Doubly.add_begin(10)
Doubly.print_LL()

print("\n")

x = Doubly.Doubly_Length()
print("NODE LENGTH IS ", x)

print("==============================================================")
print("\n ADD ENDING\n")

Doubly.add_end(2000)
Doubly.add_end(3000)
Doubly.add_end(4000)
Doubly.print_LL()

print("\n")

x = Doubly.Doubly_Length()
print("NODE LENGTH IS ", x)

print("==============================================================")
print("\n ADD POS\n")

Doubly.add_nodePosition(1, 50)
Doubly.add_nodePosition(3, 500)
Doubly.add_nodePosition(5, 1500)
Doubly.print_LL()

print("\n")

x = Doubly.Doubly_Length()
print("NODE LENGTH IS ", x)

print("==============================================================")
print("\n REMOVE BEGINNING\n")
Doubly.remove_begin()
Doubly.print_LL()

print("\n")

x = Doubly.Doubly_Length()
print("NODE LENGTH IS ", x)

print("==============================================================")
print("\n REMOVE END\n")

Doubly.remove_end()
Doubly.print_LL()

print("\n")

x = Doubly.Doubly_Length()
print("NODE LENGTH IS ", x)

print("==============================================================")
print("\n REMOVE POS\n")

Doubly.remove_nodePosition(1)
Doubly.print_LL()

print("\n")

x = Doubly.Doubly_Length()
print("NODE LENGTH IS ", x)

print("==============================================================")
print("\n FOREWORD \n")

Doubly.print_LL()

print("==============================================================")
print("\n BACKWARD \n")

Doubly.print_LL_reverse()

print("==============================================================")
print("\n SEARCHING \n")

y=Doubly.search_given(1)
print("1st node is",y)
y=Doubly.search_given(2)
print("2nd node is",y)
y=Doubly.search_given(4)
print("4th node is",y)



