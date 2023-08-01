#Doubly linked list
#creating a node class
class node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
#creating doubly class
class doublyll:
    def __init__(self):
        self.head=None
    #to print the linked list
    #forward traversing          
    def print__ll1(self):
        if self.head == None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.nref 
    #reverse transversing
    #to print the linked list          
    def print__ll1reverse(self):
        if self.head == None:
            print("linked list is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.ref
            while n is not None:
                print(n.data,"-->",end=" ")
                n.pref 
    #adding element in begining of the linked list           
    def add_begin(self,data):
        new_node=node(data)
        new_node.nref=self.head
        self.head=new_node
    #addind element at the end of the linked list   
    def add_end(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.nref != None:
                n=n.nref
            n.nref=new_node    
dll=doublyll()      
dll.add_begin(10)
dll.add_begin(5)   
dll.add_end(15)      
dll.print__ll1()
