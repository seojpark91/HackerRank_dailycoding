def countSort(arr):
    # change string to integer
    for sublist in arr:
        sublist[0] = int(sublist[0])
    
    # change first half of the strings in the input with '-'
    for i in range(n//2):
        arr[i][1] = '-'
    
    output = [[] for _ in range(n)]
    for sublist in arr:
        output[sublist[0]].append(sublist[1])
        
    print(' '.join(item for sublist in output for item in sublist))