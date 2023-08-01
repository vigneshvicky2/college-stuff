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
dll=doublyll()      
dll.print__ll1()         