from collections import OrderedDict
from collections import defaultdict

def anagrams(s1, s2):
    s1 += "!"
    s2 += "!"
    i = 0 
    j = 0
    dict1 = {}
    dict2 = {} 
    while j < len(s1):
        if s1[j]  == s1[i]:
            j += 1
        else: 
            if s1[i] in dict1:
                num += j-i
                dict1.update({s1[i] : num})
                i = j
            else:
                num = j - i
                dict1.update({s1[i] : num})        
                i = j
    i = 0 
    j = 0
    while j < len(s2):
        if s2[j]  == s2[i]:
            j += 1
        else: 
            num = j - i
            dict2.update({s2[i] : num})      
            i = j
    dict3 = OrderedDict(sorted(dict1.items()))
    dict4 = OrderedDict(sorted(dict2.items()))
    dict3 = dict(dict3)
    dict4 = dict(dict4)
    print(dict3)
    print(dict4)
    if dict4 == dict3:
        print("True")
        return True
    print("False")
    return False
      
anagrams('monkeyswrite', 'newyorktimes')

from collections import OrderedDict

def anagrams(s1, s2):
    s1 += "!"
    s2 += "!"
    i = 0 
    j = 0
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)
    
    while j < len(s1):
        if s1[j] == s1[i]:
            j += 1
        else: 
            num = j - i
            dict1[s1[i]] += num
            i = j
    
    i = 0 
    j = 0
    while j < len(s2):
        if s2[j] == s2[i]:
            j += 1
        else: 
            num = j - i
            dict2[s2[i]] += num
            i = j
    
    if dict1 == dict2:
        print("True")
        return True
    print("False")
    return False

anagrams('paper', 'reapa')

