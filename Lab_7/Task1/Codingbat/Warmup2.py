#1

def string_times(str, n):
    return str * n

#2

def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result += str[:i+1]
    return result

#3

def array_front9(nums):
    return 9 in nums[:4]

#4

def front_times(str, n):
    front = str[:3]
    return front * n

#5

def last2(str):
    count = 0
    end = str[-2:]
    
    for i in range(len(str)-2):
        if str[i:i+2] == end:
            count += 1
            
    return count

#6

def array123(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

#7

def string_bits(str):
    return str[::2]

#8

def string_match(a, b):
    count = 0
    length = min(len(a), len(b))
    
    for i in range(length-1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
            
    return count

#9

def string_match(a, b):
    count = 0
    length = min(len(a), len(b))
    
    for i in range(length-1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
            
    return count
