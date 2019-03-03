def jumpingOnClouds(c):
    jumps = i = 0
    
    while i < len(c)-1:
        if i+2 < len(c) and c[i+2] !=1:
            i +=1
        jumps +=1
        i +=1
    return jumps

jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]), jumpingOnClouds([0, 0, 0, 1, 0, 0])
