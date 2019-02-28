def cutTheSticks(arr):
    res = []
    len_stick = len(arr)
    res.append(len_stick)
    
    while arr:
        arr = [num-min(arr) for num in arr]
        arr = list(filter(lambda num: num!=0, arr))
        if len(arr) == 0:
            return res
        res.append(len(arr))    

cutTheSticks([5, 4, 4, 2, 2, 8]), cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1])