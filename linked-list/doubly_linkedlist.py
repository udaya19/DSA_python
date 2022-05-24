#double linked list
class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def traversal(self):
        if self.head is None:
            print("Double Linked List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,end=' ')
                temp = temp.next
    def insert_beg(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head.prev = nb
        self.head = nb
    def insert_end(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = ne
        ne.prev = temp
    def insert_st_spec_position(self,data,position):
        nsp = Node(data)
        temp = self.head
        a = self.head.next
        for i in range(1,position-1):
            temp = temp.next
            a = a.next
        temp.next = nsp
        nsp.prev = temp
        nsp.next = a
        a.prev = nsp
    
    def deletion_beg(self):
        temp = self.head
        a = self.head.next
        self.head = a
        temp.next = None
        a.prev = None
    
    def deletion_end(self):
        temp = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            temp = temp.next
        temp.next = None
        a.prev = None
    def deletion_at_spec_position(self,position):
        temp = self.head.next
        a = self.head
        for i in range(1,position-1):
            a = a.next
            temp = temp.next
        a.next = temp.next
        temp.next.prev = a
        temp.next = None
        temp.prev = None

n1 = Node(5)
dll = DoubleLinkedList()
dll.head = n1
n2 = Node(10)
n1.next = n2
dll.traversal()
print()
print("Doubly Linked list after insertion at beginning:")
dll.insert_beg(0)
dll.traversal()
print()
print("Doubly Linked list after insertion at end:")
dll.insert_end(15)
dll.traversal()
print()
print("Doubly Linked list after insertion at specific position:")
dll.insert_st_spec_position(2,2)
dll.traversal()
print()
print("Doubly Linked list after deletion at beginning:")
dll.deletion_beg()
dll.traversal()
print()
print("Doubly Linked list after deletion at end:")
dll.deletion_end()
dll.traversal()
print()
print("Doubly Linked list after deletion at specific position:")
dll.deletion_at_spec_position(2)
dll.traversal()