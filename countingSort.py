def countingSort(arr):
    """
    Given a list of integers, count and output the number of times each value appears as a list
    
    Parameter:
    arr : an array of integers
    
    Constraints:
    100 <= n <= 10^6
    0 <= arr[i] < 100
    """
    res = [0] * 100
    for num in arr:
        res[num] += 1

    return res