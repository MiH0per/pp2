#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums): 
    prev = nums[0]
    for i in range(1, len(nums)):
        if prev == 3 and nums[i] == 3:
            return True
        prev = nums[i]
    return False      

liks = [1,3,1,1,3,2,1,3,2,3,1,2]

print(has_33(liks))       

    