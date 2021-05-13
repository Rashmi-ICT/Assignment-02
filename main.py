from DoublyLinkedList import DoublyLinkedList

Doubly = DoublyLinkedList()

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
Doubly.print_LL()
