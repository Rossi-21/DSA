def create_linked_list(values):
    dummy_head = Node(None)
    tail = dummy_head
    
    for val in values:
        tail.next = Node(val)
        tail = tail.next
    return dummy_head.next

# recursive solution 1
def create_linked_list(values):
    if len(values) == 0:
        return None
    head = Node(values[0])
    head.next = create_linked_list(values[1:])
    return head

# recursive solution 2
def create_linked_list(values, i = 0):
    if i == len(values):
        return None
    head = Node(values[i])
    head.next = create_linked_list(values, i + 1)
    return head