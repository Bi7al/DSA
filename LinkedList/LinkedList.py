class Node :
    def __init__(self,data):
        self.data = data;
        self.next = None;
    
    
def AddNode(head):
    data = input("Enter Node Data : ")
    newNode = Node(data);
    currentNode = head;
    if(currentNode == None):
        head = newNode;
        return head;
    
    while currentNode.next:
        currentNode = currentNode.next;
    currentNode.next = newNode
    return head;
def RemoveNode(head,nodeId): # Node data is Node id 
    currentNode=prevNode = head;
    if(currentNode == None):
        print("List is Empty");
    elif head.data == nodeId:
        head = head.next;
        return head;
    else:
        while currentNode:
            if currentNode.data == nodeId :
                prevNode.next = currentNode.next;
                return head;
            prevNode = currentNode;
            currentNode = currentNode.next;
    
menu  = """
1.Add New Node
2.Remove Node
3. Print List
4.Exit\n: """

continueLoop = True;
head = None;
while continueLoop == True:
    userChoice = int(input(menu));
    if userChoice == 1 :
       head = AddNode(head);
    elif userChoice == 2:
        nodeId = input("Enter NodeId (Node Id is Node Data) : ");
        head = RemoveNode(head,nodeId);
    
    elif userChoice == 3:
        currentNode = head;
        if currentNode == None:
            print('No List present');
            pass;
        while currentNode:
            print(currentNode.data,end="->")
            currentNode = currentNode.next;
        print("X")
    
    elif userChoice == 4:
        break;
    else:
        print(" Worng Input")
    

    
    
     
    