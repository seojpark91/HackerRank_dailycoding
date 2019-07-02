def insertionSort2(n, arr):
    """
    n: an integer, the size of arr
    arr: an array of integers to sort
    """
    for i in range(1, n):
        # save current value
        curr = arr[i] 
        # save previous index for comparison
        prev_idx = i-1
        # until previous index value is greater than 0 and previous value is greater than current value, move values to the front
        while prev_idx>=0 and arr[prev_idx] > curr:
            arr[prev_idx+1] = arr[prev_idx]
            prev_idx = prev_idx-1
        # if previous index hasn't changed, the list will remain the same
        arr[prev_idx+1] = curr
        print(' '.join(map(str, arr)))

if __name__ == '__main__':
    insertionSort2(6, [1, 4, 3, 5, 6, 2])
    
