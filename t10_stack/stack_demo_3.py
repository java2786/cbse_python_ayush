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
        
    def push(self, data):
        if(self.size == self.max_size):
            print("Overflow")
        else:
            self.list.append(data)
            self.size = self.size+1
       
    def size(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.max_size
    
    def show(self):
        # print("Capacity:",self.max_size,"Size:",self.size,"Stack:",self.list)
        for i in range(len(self.list)):
            print(f"{self.list[i]}->",end="")
        print("Top")
            
    
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
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
myStack.show()
