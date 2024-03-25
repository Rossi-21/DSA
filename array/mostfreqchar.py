# My Solution
def most_frequent_char(s):
    char = {}
    # iterate through the string
    for i in s:
        if i not in char:
            char[i] = 0  
        # create a hash map of letters and frequency    
        char[i] += 1 
    print(char)
    # return the first letter that occurs most often
    
    largest = 0
    result = None
    
    for key, value in char.items():
        if value > largest:
            largest = value
            result = key
    print(result)
    return result

# Solution 1
def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0    
        count[char] += 1
        
    best = None
    for char in s:
        if best is None or count[char] > count[best]:
            best = char
    return best

most_frequent_char('bookeeper')

# Solution 2
from collections import Counter

def most_frequent_char(s):
    count = Counter(s)
    best = None
    for char in s:
        if best is None or count[char] > count[best]:
            best = char
    return best