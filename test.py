# Write a function, uncompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:
# <number><char>
# for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.

def uncompress(s):
    numbers = "0123456789"
    results = []
    i = 0
    j = 0
    # iterate through s 
    while j < len(s):
        # if the j index of s is in the numbers string
        if s[j] in numbers:
            # increment j
            j += 1
        # if the j index of s is not in the number string
        else:
            # create a number variable between the i index and the j index of s and turn it in to and integer
            num = int(s[i:j])
            # the j index of s should be an alphbetic character. Multiply it by num and append it to the results list
            results.append(s[j] * num)
            # increment j
            j += 1
            # bring i to the start of the next number sequence
            i = j
    # return results as a string        
    return ''.join(results)

# n = number of groups
# m = max num found in any group
# Time: O(n*m)
# Space: O(n*m)
    