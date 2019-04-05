def beautifulTriplets(d, arr):
    count = 0
    for num in arr:
        num_2 = num + d
        
        if num_2 in arr and num_2 + d in arr:
            count +=1
    return count

beautifulTriplets(3, [1, 6, 7, 7, 8, 10, 12, 13, 14, 19])