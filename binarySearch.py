def test_location(cards, query, mid):
    mid_number = cards[mid]
    
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'
    
def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        
        if result == query:
            return mid
        elif result < query:
            hi = mid -1
        elif result > query:
            lo = mid + 1
            
    return -1