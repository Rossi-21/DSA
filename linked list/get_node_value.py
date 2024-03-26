class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d



# My solution
def get_node_value(head, index):
    current = head
    counter = 0
    while current is not None:
        if counter == index:
            return current.val
        counter += 1
        current = current.next
    return None

get_node_value(a, 2)

# Recursive solution
def get_node_value(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val
    
    return get_node_value(head.next, index-1)
    