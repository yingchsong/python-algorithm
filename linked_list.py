class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Linked_list(object):
    def __init__(self):
        self.head=None
        self.length=0

    def add_node(self,node):
        if self.length==0:
            self.head=node
            self.length+=1
        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=node
            self.length+=1
    
    def show_llist(self):
        temp=self.head
        while temp.next!=None:
            print(temp.data)
            temp=temp.next
        print(temp.data)
        pass
    





ll=Linked_list()
for i in range(10):
    ll.add_node(Node(i))
ll.show_llist()



