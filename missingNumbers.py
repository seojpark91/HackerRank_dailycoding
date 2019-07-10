def missingNumbers(arr, brr):
    """
    return a sorted array of missing numbers
    
    parameters:
    arr: the array with missing numbers
    brr: the original array of numbers
    """
    c_arr = Counter(arr)
    c_brr = Counter(brr)
    res = []
    for num in c_brr:
        if num not in c_arr:
            res.append(num)
        elif (num in c_arr) and (c_arr[num] != c_brr[num]):
            res.append(num)
    return sorted(res)