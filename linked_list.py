class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Linked_list(object):
    def __init__(self):
        self.head=None
        self.length=0

    def tailadd_node(self,node):
        if self.length==0:
            self.head=node
            self.length+=1
        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=node
            self.length+=1

    def headadd_node(self,node):
        if self.length==0:
            self.head=node
            self.length+=1
        else:
            temp=self.head
            self.head=node
            self.head.next=temp
            self.length+=1
    
    def anyadd_node(self,node,idx):
        # num is the situation need to be added
        if self.length>idx:
            temp=self.head
            for i in range(idx-1):
                temp=temp.next
            node.next=temp.next
            temp.next=node


    def search_node(self,node):
        if self.length==0:
            return False
        else:
            flag=0
            temp=self.head
            while temp.next != None:
                if temp.data==node.data:
                    flag+=1
                    break
                else:
                    temp=temp.next
            if temp.data==node.data:
                flag+=1
            if flag>0:
                return True
            else:
                return False
    # the cost of this sort is high!
    def sort_list(self):
        cnt=[]
        temp=self.head
        while temp.next!=None:
            cnt+=[temp.data]
            temp=temp.next
        cnt+=[temp.data]
        cnt=sorted(cnt)
        temp=self.head
        i=0
        while temp.next!=None:
            temp.data=cnt[i]
            i+=1
            temp=temp.next
        temp.data=cnt[-1]
        
    
    def show_llist(self):
        temp=self.head
        while temp.next!=None:
            print(temp.data,end='->')
            temp=temp.next
        print(temp.data)
        pass
    




###test part
ll=Linked_list()
for i in range(10):
    ll.tailadd_node(Node(i))
ll.headadd_node(Node(9))
ll.show_llist()
##search node
if ll.search_node(Node(12)):
    print('yes')
else:
    print('no')
##add node in any situation
ll.anyadd_node(Node(15),5)
ll.show_llist()

ll.sort_list()
ll.show_llist()