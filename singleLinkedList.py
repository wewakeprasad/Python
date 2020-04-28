class Node:
    def __init__ (self,value):
        self.value = value
        self.next = None


class List:
    def __init__ (self,value):
        self.head = Node(value)

    def insert (self,value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value) 

    def show(self):
        current = self.head
        while (current):
            print(current.value)
            current = current.next


a = List(0)
a.insert(10)
a.insert(20)
a.insert(30)
a.show()
