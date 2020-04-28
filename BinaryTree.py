class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self,value):
        #node value is already set  -> starts traversing 
        if self.value:
            #left
            if value < self.value:
                #To set a new value ,make a new node
                if self.left is None:
                    self.left = BinaryTree(value)
                #if left value is already set ,call insert on left
                else:
                    self.left.insert(value)
            #right
            else:
                #value > self.value
                #To set a new right value ,make a new node
                if self.right is None:
                    self.right = BinaryTree(value)
                    # if right value is already set,call insert() on right
                else:   
                    self.right.insert(value)
        else: #if value is not set
            self.value = value


    def printInOrder(self):
        if self.left:
            self.left.printInOrder()
        print (self.value)
        if self.right:
            self.right.printInOrder()

if __name__ == '__main__':
    root = BinaryTree('F')
    root.insert('B')
    root.insert('G')
    root.insert('A')
    root.insert('D')
    root.insert('I')
    root.insert('C')
    root.insert('E')
    root.insert('H')
    root.printInOrder()

