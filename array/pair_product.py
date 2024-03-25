def pair_product(numbers, target_product):
    previous = {}
    
    for index, num in enumerate(numbers):
        complement = target_product / num
        if complement in previous:
            return (previous[complement], index)
        previous[num] = index

pair_product([3, 2, 5, 4, 1], 8)