# My Solution
def linked_list_find(head, target):
    list = []
    current = head
    while current is not None:
        list.append(current.val)
        current = current.next
    if target not in list:
        return False
    return True

# My Solution 2
def linked_list_find(head, target):
    current = head
    while current is not None:
        if current.val == target:
            return True
        current = current.next
    return False

# Recursive Solution
def linked_list_find(head, target):
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find(head.next, target)