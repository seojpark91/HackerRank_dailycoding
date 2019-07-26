def maximumPerimeterTriangle(sticks):
    """
    return an array of integers that represent the side lengths of the chosen triangle in non-decreasing order
    
    parameter:
    sticks: an integer array that represents the lengths of sticks available
    """
    n = len(sticks)
    idx = n-3
    # sort the given array 
    sticks = sorted(sticks)
    # until we find the valid triangle which has the maximum length
    while idx >= 0 and (sticks[idx] + sticks[idx+1] <= sticks[idx+2]):
        idx -= 1
    
    if idx >=0:
        return [sticks[idx], sticks[idx+1], sticks[idx+2]]
    else:
        return [-1]