def surfaceArea(A):
    """
    A : the board with stacked number of cubes at each position
    """
    # Pad the board with a layer of 0 for easier calculation
    padded_A = [[0] * (len(A[0]) + 2)]
    for row in A:
        padded_A.append([0] + row + [0])
    padded_A.append([0] * (len(A[0]) + 2))
    # Bottom and top area
    res = len(A) * len(A[0]) * 2
    
    # calculate side area which is the sum of differences between adjacent cells
    for i in range(1, len(padded_A)):
        for j in range(1, len(padded_A[i])):
            res += abs(padded_A[i][j] - padded_A[i-1][j])
            res += abs(padded_A[i][j] - padded_A[i][j-1])
    return res