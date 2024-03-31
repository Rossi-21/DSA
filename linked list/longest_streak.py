def longest_streak(head):
    max_streak = 0
    current_streak =  0 
    current_node = head
    previous = None
    while current_node is not None:
        if current_node.val == previous:
            current_streak += 1
        else:
            current_streak = 1
        previous = current_node.val
        if current_streak > max_streak:
            max_streak = current_streak
        
        current_node = current_node.next

        return max_streak
    
    # recursive solution
    
