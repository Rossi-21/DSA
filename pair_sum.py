def pair_sum(numbers, target_sum):
    i = 0
    j = 0
    # iterate through the array
    while j < len(numbers)-1:
        j+=1
        print(numbers[i], numbers[j])
        sum = numbers[j] + numbers[i]
        print('sum = ' + str(sum))
        # check if numbers in the array sum to the target
        if sum  == target_sum:
            result = (i,j)
        if j == len(numbers)-1:
            i+=1
            j=i
        else:
            print('nope')
    # retrun the indices in a tuple
    print(result)
    return result

pair_sum([1, 6, 7, 2], 13) 