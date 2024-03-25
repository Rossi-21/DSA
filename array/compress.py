# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string 
# where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.
# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'
# You can assume that the input only contains alphabetic characters.

def compress(s):
    # Add a non-alphnumeric charecter to the end of the string so that j can continue to iterate after the initial string
    s += '!'
    i = 0
    j = 0
    results = []
    # iterate though the string 
    while j < len(s):
        # If the indecies are the same , increment j
        if s[j] == s[i]:
            j += 1
        # If the indecies are different
        else:
            # Create a number variable equal to the position of j minus the position of i
            num = j-i
            # If the number is 1 only add the letter or index of i to the array
            if num == 1:
                results.append(s[i])
            # If the number is not 1 add both the number and the letter to the array
            else:
                results.append(str(num))
                results.append(s[i])
            # move i to j's position and start again
            i = j
    print(''.join(results)) 
    # Join the contents of the array into a string and return it.       
    return ''.join(results)

compress('ccaaatsss')

# n = length of string
# Time: O(n)
# Space: O(n)