''' 
@author:  Arvind A. de Menezes Pereira
@since:  Jul 13, 2013
@summary: Building a singly-linked linked list and then reversing it.
'''
class Node:
    def __init__(self,data=None ):
        self.data = data
        self.next = None
        
    def __iter__(self):
        return self
    
    def next(self):
        if self.next == None:
            raise StopIteration
        else:
            temp = self
            self = self.next
            return temp

''' # Recursive insert.. 
def insert(head,data):
    if head == None:
        head = Node( data )
        return head
    else:
        head.next = insert( head.next, data )
    return head
'''   
     
def insert( head, data ):
    while( head != None ):
        head = head.next
    head = Node(data)
    return head

def reverseList( head ):
    curr = head
    prev = None
    
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev

def printList( head ):
    curr = head
    while curr!= None:
        print curr.data
        curr = curr.next
        
def findLength( curr ):
    len = 0
    head = curr
    while( head!=None ):
        len+=1
        head = head.next
    return len


def findOverlappingNode( head1, head2 ):
    ''' Assuming two lists overlap at some point,
        find the point of overlap '''
    curr1, curr2 = head1, head2
    n1, n2 = findLength( head1 ), findLength( head2 )
    
    if curr1==curr2:
        if curr1==None:
            return None
        else:
            return curr1.data

    if n1 < n2 :
        for i in range(n2-n1):
            if curr1.next==curr2.next and curr1.next!=None:
                return curr1.next.data
            curr2 = curr2.next
    elif n2 < n1:
        for i in range(n1-n2):
            if curr1.next==curr2.next and curr:
                return curr1.next.data
            curr1 = curr1.next
                
    while curr1!=None and curr2!=None:
        if curr1==curr2:
            return curr1.data
        curr1 = curr1.next
        curr2 = curr2.next
    
    return None
    

if __name__=='__main__':
    head = Node(0)
    curr = head
    x = [ i*i for i in range(1,10)]
    for data in x:
        curr.next = insert(head,data)
        curr = curr.next

    head2 = Node(0)
    curr2 = head2
    y = [ i**3 for i in range(1,5) ]
    for data in y:
        curr2.next = insert( head2, data)
        curr2 = curr2.next
    
    printList( head2 )
    head2.next.next.next = head.next.next.next.next.next.next
    print
    printList(head2)
    
    print 'Overlapping Node has data:',findOverlappingNode(head, head2)
    
    printList( head )
    print
    tail = reverseList( head )
    printList( tail )
    
    head = reverseList( tail )
    print
    printList( head )
    
    
        