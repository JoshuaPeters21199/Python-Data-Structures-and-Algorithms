class Stack:
    def __init__(self):
        self.__index = []

    def __len__(self):
        return len(self.__index)
    
    def push(self, item):
        self.__index.insert(0, item)

    def peek(self):
        if len(self) == 0:
            raise Exception("peek() called on empty stack")
        return self.__index[0]
    
    def pop(self):
        if len(self.__index) == 0:
            raise Exception("pop() called on empty stack")
        return self.__index.pop(0)
    
    def __str__(self):
        return str(self.__index)

def main():
    s = Stack()
    print(s.__len__())
    s.push(7)
    s.push(1)
    s.push(1)
    print(s)
    print(s.peek())
    s.pop()
    print(s)

if __name__ == "__main__":
    main()