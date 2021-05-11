from DoublyLinkedList import DoublyLinkedList

d = DoublyLinkedList()
'''d.add_begin(89)
d.add_begin(90)
d.add_begin(00)'''

d.add_begin(90)
d.add_begin(00)
d.add_end(2222)
d.add_end(567)

print("\n")
x = d.Doubly_Length()
print("length",x)
print("\n")

d.add_nodePosition(6,34)

'''d.remove_begin()
d.remove_end()'''
d.print_LL()
d.print_LL_reverse()
d.remove_nodePosition(3)

d.print_LL()
d.print_LL_reverse()

print(d.len)
print("\n")

'''print(d.search_given(3))'''

print("\n")
x = d.Dobly_Length()
print("length",x)

