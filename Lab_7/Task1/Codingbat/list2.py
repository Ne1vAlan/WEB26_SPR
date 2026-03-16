#1

def count_evens(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count

#2

def sum13(nums):
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1
    return total

#3

def big_diff(nums):
    return max(nums) - min(nums)

#4

def sum67(nums):
    total = 0
    ignore = False

    for n in nums:
        if n == 6:
            ignore = True
        elif ignore and n == 7:
            ignore = False
        elif not ignore:
            total += n

    return total

#5

def centered_average(nums):
    nums = sorted(nums)
    nums = nums[1:-1]
    return sum(nums) // len(nums)

#6

def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False