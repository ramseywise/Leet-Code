"""LeetCode Functions."""

# Problem 1
def twoSumI(nums, target):
    """ Return the indices of two numbers in a list that equal the target."""
    values = dict() # use dict to map complement of value to index it corresponds 
    for i, j in enumerate(nums): # map value j to index i
        val = target - j # calculate corresponding value
        if val > 0 and val in values: # check if value is positive and in dict
            return [values[val], i] # if so, return index position of nums for value j in dict
        values[j] = i # if corresponding value is not in dict, continue to second value in dict
        
    return []  # if no solution found, return emptyt list

# Problem 1a
def twoSum(nums, target):
    """ Return two numbers in a list that equal the target."""
    values = dict() # use dict to map complement of value to index it corresponds 
    for i, j in enumerate(nums): # map value j to index i
        val = target - j # calculate corresponding value
        if val > 0 and val in values: # check if value is positive and in dict
            return val, j # if so, return index position of nums for value j in dict
        values[j] = i # if corresponding value is not in dict, continue to second value in dict
        
    return []  # if no solution found, return emptyt list

# Problem 9
def isPalindrome(x):
    """Assert whether number reads the same backwards and forwards."""
    
    return str(x) == str(x)[::-1] # convert to str, count down beginning to end by 1

# Problem 9a
def everyOdd(x):
    """Assert whether number reads the same backwards and forwards."""
    
    return str(x)[::2] # convert to str, count down beginning to end by 1
