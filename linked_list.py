class Node:
    data= None
    next_node=None
    
    def __init__(self,data):
        self.data=data
        
    def __repr__(self):
        return "i am %s"% self.data
    
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head==None
    
    def know_size(self):
        current=self.head
        count=0
        while current !=None:
            count +=1
            current=current.next_node
        return count
    
    def add_list(self ,data):
        new_node=Node(data)
        new_node.next_node=self.head
        self.head =new_node
       

    def search_list(self,target):
        current=self.head
        
        while current !=None:
            if current.data == target:
                return current
            else:
                current=current.next_node
        return None
        
    def insert_node(self,insert,position):
        if position == 0:
            self.add_list(insert)
        pass 
        
        
        
        
        
        
        
        
    def __repr__(self):
        
        nodes=[]
        current=self.head
        
        while current !=None:
            if current is self.head:
                nodes.append("[Head %s]" % current.data)
            if current.next_node is None:
                nodes.append("[Tail %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
                
            current=current.next_node
        return '->' .join(nodes)

                    
                