def balancedSums(arr):
    """
     This function find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right. 
     
     It returns a string, either YES if there is an element meeting the criterion or NO otherwise.
     
     parameter:
     arr : an array of integers
    """
    initial_sum_left = sum(arr[:0])
    initial_sum_right = sum(arr[1:])
    
    if sum_left == sum_right:
        return "YES"
    else:
        for i, _ in enumerate(arr[:-1]):
            initial_sum_left += arr[i]
            initial_sum_right -= arr[i+1]
            if initial_sum_left == initial_sum_right:
                return "YES"
    return "NO"