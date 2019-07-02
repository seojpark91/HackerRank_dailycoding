def insertionSort1(n, arr): 
    """
    n: an integer, the size of arr
    arr: an array of integers to sort
    
    brute force method
    This function prints interim arrays and the final array during sorting
    """
    e = arr[-1]
    index = n-2
    while (e < arr[index]) and (index >=0):
        arr[index+1] = arr[index]
        print(' '.join(map(str, arr)))
        index -=1
    arr[index+1] = e
    print(' '.join(map(str, arr)))