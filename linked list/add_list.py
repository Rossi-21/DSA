def add_lists(head_1, head_2, carry = 0):
    if head_1 is None and head_2 is None:
        return None
    
    val_1 = 0 if head_1 is None else head_1.val
    val_2 = 0 if head_2 is None else head_2.val
    
    sum = val_1 + val_2 + carry
    carry = 1 if sum > 9 else 0
    
    digit = sum % 10
    result_node = Node(digit)
    
    next_1 = None if head_1 is None else head_1.next
    next_2 = None if head_2 is None else head_2.next
    
    result_node.next = add_lists(next_1, next_2, carry)
    return result_node