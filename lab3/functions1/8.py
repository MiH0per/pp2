#Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):    
    correct_order = [0, 0, 7]
    current_order = []
    for i in range(len(nums)):
        if (nums[i] == correct_order[len(current_order)]):
            current_order.append(nums[i])
            
        if current_order == correct_order:
            return True
    return False

print(spy_game([1,2,4,0,7,5]))