def pair_sum(numbers, target_sum):
    i = 0
    j = 0
    # iterate through the array
    while j < len(numbers)-1:
        j+=1
        print(numbers[j], numbers[i])
        sum = numbers[j] + numbers[i]
        print('sum = ' + str(sum))
        # check if numbers in the array sum to the target
        if sum  == target_sum:
            result = (i,j)
        else:
            print('nope')
        
    
    # retrun the indices in a tuple
    print(result)
    return result

pair_sum([4, 7, 9, 2, 5, 1], 3) # -> (3, 5)