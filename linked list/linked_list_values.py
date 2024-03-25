# Solution 1
def linked_list_values(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values

# Recursive Solution
def linked_list_values(head):
    values = []
    _linked_list_values(head, values)
    return values

def _linked_list_values(head, values):
    if head is None:
        return
    values.append(head.val)
    _linked_list_values(head.next, values)