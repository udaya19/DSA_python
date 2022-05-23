#Creating new node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



#Creating Singly linked list
class SinglyLL:
    def __init__(self):
        self.head = None
    def traversal(self):
        if self.head is None:
            print("SLL is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=' ')
                temp = temp.next
    def insert_beg(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    def insert_end(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = ne
    def insert_at_specific_position(self,data,position):
        nsp = Node(data)
        temp = self.head
        for i in range(1,position-1):
            temp = temp.next
        nsp.next = temp.next
        temp.next = nsp
    def deletion_beg(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
    def deletion_end(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
    def deletion_spec_position(self,position):
        temp = self.head.next
        prev = self.head
        for i in range(1,position):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None
    
sll = SinglyLL()
n1 = Node(5)
sll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15) 
n2.next = n3
n4 = Node(20)
n3.next = n4
sll.traversal()
print()
print("Insertion:")
sll.insert_beg(0)
print()
print("Linked List After Inserting value at beginning")
sll.traversal()
sll.insert_end(25)
print()
print("Linked List After Inserting value at end")
sll.traversal()
sll.insert_at_specific_position(2,2)
print()
print("Linked List After Inserting value at specific position")
sll.traversal()
print()
print("Deletion:")
print("Deletion at beginning")
sll.deletion_beg()
sll.traversal()
print()
print("Deletion at end")
sll.deletion_end()
sll.traversal()
print()
print("Deletion at specific position")
sll.deletion_spec_position(0)
sll.traversal()