class Queue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception("dequeue() called on empty queue")
        self.queue.pop(0)

    def peek(self):
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)
    
def main():
    q = Queue()
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    print(q)
    print(q.size())
    q.dequeue()
    print(q)
    print(q.size())
    print(q.isEmpty())
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    print(q.isEmpty())

if __name__ == "__main__":
    main()