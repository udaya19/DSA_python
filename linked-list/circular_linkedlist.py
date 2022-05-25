#circular_linkedlist.py

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

cll = CircularLinkedList()
cll.addList(10)
cll.addList(20)
cll.addList(30)
cll.addList(40)
cll.traversal()