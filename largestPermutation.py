def largestPermutation(k, arr):
    """
    return an array that represents the highest value permutation that can be formed
    
    parameters:
    k: an integer that represents the limit of swaps
    arr: an array of integers
    """
    # "perfect" array is the reversed ordered array
    compare_arr = sorted(arr, reverse = True)
    if arr == compare_arr:
        return arr
    # make dictionary to look up index 
    index_dict = {n:i for i, n in enumerate(arr)}
    
    for idx, num in enumerate(compare_arr):
        if arr[idx] != num:
            # keep track of how many swaps would be needed by comparing with the reversed ordered array
            k -=1
            # get index of the original array to swap
            swap_idx = index_dict[num]
            # swap indices
            arr[idx], arr[swap_idx] = num, arr[idx]
            # also update index dictionary
            index_dict[num] = idx
            index_dict[arr[swap_idx]] = swap_idx
            if k == 0:
                return arr
    return arr