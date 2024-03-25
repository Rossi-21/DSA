# Iterative Solution
def sum_list(head):
    sum = 0
    current = head
    while current is not None:
        sum += current.val
        current = current.next
    return sum
# Recusive solution
def sum_list(head):
    if head is None:
        return 0
    head.val += sum_list(head.next)
    