class Stack :
    def __init__(self):
        self.stack =[];
    def isEmpty(self):
        if len(self.stack) == 0 :
            return True;
        else :
            return False;
    def pop(self):
        if (self.isEmpty()):
            return "Stack is Empty";
        else:
            data = self.stack[len(self.stack)-1]; # Get the top Element    Not using pop deliberatly !!!!!
            self.stack.pop();
            return data ;
    def push(self,data):
        self.stack.append(data);
    def peek(self):
        if (self.isEmpty()):
            return "Stack is Empty";
        else :
            return self.stack[-1];
    def size(self):
        return len(self.stack)



myStack = Stack();
myStack.push(1);
myStack.push(2);
myStack.push(3);
myStack.push(4);
myStack.push(5);
myStack.push(6);
print(myStack.peek());
print(myStack.pop());
print(myStack.peek());
print(myStack.size());
print(myStack.isEmpty())
