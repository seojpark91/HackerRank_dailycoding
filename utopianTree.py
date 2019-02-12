def utopianTree(n):
    height = 1
    
    for i in range(0,n+1):
        if i == 0:
            height +=0
        elif i%2:
            height = 2 * height
        else:
            height +=1
    return height