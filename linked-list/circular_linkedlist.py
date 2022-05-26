#circular_linkedlist.py

from tkinter import N


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None 
    def addList(self,data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            node = Node(data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head
    def traversal(self):
        if self.head is None:
            print("SLL is empty")
        else:
            temp = self.head
            while temp.next != self.head:
                print(temp.data, end=' ')
                temp = temp.next
            print(temp.data)
    
    def insert_beg(self,data):
        nb = Node(data)
        nb.next = self.head
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = nb
        self.head = nb
    def insert_end(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = ne
        ne.next = self.head
    # def delete_beg(self):
    #     temp = self.head
    #     # temp1 = self.head
    #     a = self.head.next
    #     self.head = a
    #     temp.next = None
    #     while temp.next != self.head:
    #         temp = temp.next
    #     temp.next = self.head
        # temp1.next = None
    def deletion_end(self):
        a = self.head.next
        temp = self.head
        while a.next != self.head:
            a = a.next
            temp = temp.next
        temp.next = self.head
        a.next = None
cll = CircularLinkedList()
cll.addList(10)
cll.addList(20)
cll.addList(30)
cll.addList(40)
cll.traversal()
cll.insert_beg(0)
cll.traversal()
cll.insert_end(50)
cll.traversal()
cll.deletion_end()
cll.traversal()