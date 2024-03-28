def zipper_lists(head_1, head_2):
    counter = 0
    tail = head_1
    cur1 = head_1.next
    cur2 = head_2
    while cur1 is not None and cur2 is not None:
        if counter % 2 == 0:
            tail.next = cur2
            cur2 = cur2.next
        else:
            tail.next = cur1
            cur1 = cur1.next
            tail = tail.next
            counter +=1
        
    if cur1 is not None:
        tail.next = cur1
    if cur2 is not None:
        tail.next = cur2
    return head_1

# recursive solution
def zipper_lists(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1
    
    next_1 = head_1.next
    next_2 = head_2.next
    head_1.next = head_2
    head_2.next = zipper_lists(next_1, next_2)
    return head_1