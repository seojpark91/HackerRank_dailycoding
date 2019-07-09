def diff(A):
    """
    Helper function for the function of closestNumbers
    
    This function finds the smallest difference in the given array
    Parameters:
    A : an array of integers
    """
    A = sorted(A)
    diff = []
    for i, _ in enumerate(A[:-1]):
        diff.append(A[i+1] - A[i])
    return min(diff), A

def closestNumbers(arr):
    """
    This function finds pairs of two values which has the smallest difference
    
    parameter:
    arr : an array of integers
    """
    
    min_diff, arr = diff(arr)
    res = []
    for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == min_diff:
                res.append(arr[i])
                res.append(arr[i+1])
    return res

