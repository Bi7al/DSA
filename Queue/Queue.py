class Queue :
    def __init__(self):
        self.queue = [];
        
        
    def isEmpty(self):
        if (len (self.queue)<1):
            return True;
        else:
            return False;
        
        
    def size(self):
        return len(self.queue);
    
    def peek(self):
        if (self.isEmpty()):
            return "Queue is Empty";
        else:
            return self.queue[0];
        
        
    def Enqueue(self,data):
        self.queue.append(data);
        
        
    def Dequeue(self):
        if(self.isEmpty()):
            return "Queue is Empty";
        return self.queue.pop(0);
        
    
myqueue = Queue();
myqueue.Enqueue(1);
myqueue.Enqueue(2);
myqueue.Enqueue(3);

print(myqueue.peek());
print(myqueue.size());
print(myqueue.Dequeue());
print(myqueue.Dequeue());
print(myqueue.Dequeue());
print(myqueue.Dequeue());
print(myqueue.size());


