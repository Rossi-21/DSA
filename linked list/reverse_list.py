# Solution 1
def reverse_list(head):
    current = head
    previous = None
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous

# Solution 2
def reverse_list(head, prev = None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list(next, head)