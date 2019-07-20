def minimumAbsoluteDifference(arr):
    """
    return an integer that represents the minimum absolute difference between any pair of elements
    n: an integer that represents the length of arr
    arr: an array of integers
    """
    sorted_arr = sorted(arr)
    return min(abs(x-y) for x, y in zip(sorted_arr, sorted_arr[1:]))