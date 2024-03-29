# my solution
def is_univalue_list(head):
    current = head
    while current is not None:
        if head.val != current.val:
            return False
        current = current.next    
    return True

# recursive solution
def is_univalue_list(head, prev_val = None):
    if head is None:
        return True
    if prev_val is not None and head.val != prev_val:
        return False
    return is_univalue_list(head.next, head.val)