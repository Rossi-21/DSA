# My Solution
def remove_node(head, target_val):
    current = head
    previous = None
    
    while current is not None:
        if current.val == target_val:
            if previous == None:
                return head.next
            else:
                previous.next = current.next
                return head
        previous = current
        current = current.next
    return head

# Iterative solution
def remove_node(head, target_val):
    if head.val == target_val:
        return head.next
    current = head
    prev = None
    
    while current is not None:
        if current.val == target_val:
            prev.next = current.next
            break
        prev = current
        current = current.next
    return head