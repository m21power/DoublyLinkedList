class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DLinked:
    def __init__(self):
        self.head=None
    def length(self):
        iter=self.head
        c=0
        while iter:
            c+=1
            iter=iter.next
        return c
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            
            if DLinked().length()==1:
                    self.head=new_node
            
            else:
                iter=self.head
                while iter.next:     
                    iter=iter.next
                iter.next=new_node
                new_node.prev=iter
    def printing(self):
        cur=self.head
        while cur:
            print(cur.data,end=' ')
            cur=cur.next
    def print_reverse(self):
        iter=self.head
        while iter.next:
            iter=iter.next
        pr=iter
        while pr:
            print(pr.data,end=' ')
            pr=pr.prev
