def runningTime(arr):
    """
    simple inversion count problem with insertion sort
    """
    inv_count = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] > arr[j]):
                inv_count +=1
    return inv_count