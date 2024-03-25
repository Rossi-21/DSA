# My solution
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

# Brute force solution
def pair_sum(numbers, target_sum):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return(i,j)

# Liniar runtime solution
def pair_sum(numbers, target_sum):
    previous_nums = {}
    
    for index, num in enumerate(numbers):
      complement = target_sum - num
      
      if complement in previous_nums:
        return (previous_nums[complement],index)
      
      previous_nums[num] = index
      
pair_sum([1, 6, 7, 2], 13) 