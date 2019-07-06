def countingSort2(arr):
    """
    with countingSort1.py algorithm, return sorted array
    
    arr: an array of integers
    """
    res = [0] * 100
    for num in arr:
        res[num] += 1
    sorted_array=[]
    for i, num in enumerate(res):
        if num !=0:
            sorted_array.append([i] * num)
    
    return [item for sublist in sorted_array for item in sublist]