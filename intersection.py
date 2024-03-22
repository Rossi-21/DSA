# My solution
def intersection(a, b):
    result = []
    set = {}
    for i in a:
        set[i] = i
    for j in b:
        if j in set:
            result.append(j)
        
    return result

# Brute Force Solution 1
def intersection(a,b):
    result = []
    for i in a:
        if i in b:
            result.append(i)
    return result

# Solution 2
def intersection(a,b):
    # Create a result array 
    result = []
    # Create a set to store items from the first list
    items_set = set()
    # Iterate through the list and add the items to the set
    for item in a:
        items_set.add(item)
    # Iterate through the second list and check for common items
    for ele in b:
        # Add the common items to the results array
        if ele in items_set:
            result.append(ele)
    return result

# Solution 3
def intersection(a,b):
    result = []
    items_set = set(a)
    for ele in b:
        if ele in items_set:
            result.append(ele)
    return result

# Solution 4
def intersection(a, b):
    # Create a set from the items in list a
    items_set = set(a)
    # Return an array that loops though list b and adds common items to the array
    return [ ele for ele in b if ele in items_set]