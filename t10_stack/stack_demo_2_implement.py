class Stack:
    max_size = 5
    def __init__(self):
        print("Stack initialized/created.")
        self.list = []
        self.size = 0
    def remove(self):
        if self.size == 0:
            print("Underflow")
            return -1
        else:
            self.size = self.size - 1
            return self.list.pop()
        
    def insert(self, data):
        if(self.size == self.max_size):
            print("Overflow")
        else:
            self.list.append(data)
            self.size = self.size+1
       
    def size(self):
        return self.size
    
    def show(self):
        print("Capacity:",self.max_size,"Size:",self.size,"Stack:",self.list)
    
    def peek(self):
        if self.size == 0:
            print("Underflow")
            return -1
        else:
            # data = self.list.pop()
            # self.list.append(data)
            # return data
            return self.list[-1]
    
myStack = Stack() 
myStack.show()
myStack.insert(1)
myStack.insert(2)
myStack.insert(3)
myStack.insert(4)
myStack.insert(5)
myStack.show()
myStack.insert(6)
myStack.show()
removed = myStack.remove()
print("Removed value is",removed)
removed = myStack.remove()
print("Removed value is",removed)
removed = myStack.remove()
print("Removed value is",removed)
removed = myStack.remove()
print("Removed value is",removed)
removed = myStack.remove()
print("Removed value is",removed)
# my stack is empty
removed = myStack.remove()
print("Removed value is",removed)
myStack.show()
