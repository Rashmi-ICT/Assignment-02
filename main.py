from DoublyLinkedList import DoublyLinkedList

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

Doubly.search_given(3)







'''
Doubly.add_begin(100)
Doubly.add_begin(200)
Doubly.add_begin(300)

Doubly.add_end(400)
Doubly.add_end(500)
Doubly.add_end(600)

Doubly.add_nodePosition(-1, 000)
Doubly.add_nodePosition(0, 111)
Doubly.add_nodePosition(1, 222)
Doubly.add_nodePosition(2, 333)
Doubly.add_nodePosition(3, 444)
Doubly.add_nodePosition(4, 555)
Doubly.add_nodePosition(5, 666)
Doubly.add_nodePosition(11, 777)

Doubly.add_end(56658)
Doubly.print_LL_reverse()

x = Doubly.Doubly_Length
print(x)

Doubly.add_nodePosition(0, 8888)
Doubly.print_LL_reverse()

Doubly.remove_begin()
Doubly.remove_end()

Doubly.remove_nodePosition(12)

Doubly.print_LL_reverse()

print()
# print("searching node prev",Doubly.searchPrev(5),"\n","searching node "Doubly.searchNode(5),"\n","searching node next",Doubly.searchNext(5))
Doubly.print_LL_reverse()
print("\n")
Doubly.print_LL()'''
