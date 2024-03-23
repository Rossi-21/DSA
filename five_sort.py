# My Solution
def five_sort(nums):
    i = 0
    j = len(nums)-1
    temp = None
    while j >= i:
        if nums[j] == 5:
            j -= 1
        elif nums[i] == 5:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        else:
            i += 1
    print(nums)
    return nums

five_sort([12, 5, 1, 5, 12, 7])

# Solution without temp
def five_sort(nums):
    i = 0
    j = len(nums)-1
    while j >= i:
        if nums[j] == 5:
            j -= 1
        elif nums[i] == 5:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        else:
            i += 1

    return nums