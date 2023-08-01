#singley linked list
#creating a node class
class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
#creating a empty linked list        
class linkedlist:
    def __init__(self):
        self.head=None
#to print the linked list          
    def print__ll1(self):
        if self.head == None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref 
 #Adding new element at the begining of the linked list                           
    def add_begin(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node 
#Adding new element at the end of the linked list        
    def add_end(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.ref != None:
                n=n.ref
            n.ref=new_node
#calling functions                
ll1=linkedlist()
ll1.add_begin(20)
ll1.add_begin(10)
ll1.add_end(30)
ll1.add_end(40)
ll1.print__ll1( )
        