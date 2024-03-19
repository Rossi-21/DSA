def anagrams(s1, s2):
    return char_count(s1) == char_count(s2)

def char_count(s):
    count = {}
    # Interate though the string
    for char in s:
        # If the character is not in the string
        if char not in count:
            # add it to the dictionary and give it a count of 0
            count[char] = 0
        # Every time the character appers increment the
        count[char] += 1
        
    return count

anagrams('paper', 'reapa')

