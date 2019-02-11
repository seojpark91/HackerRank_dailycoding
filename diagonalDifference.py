def diagonalDifference(arr):
    end = len(arr) - 1
    dlist1 = []
    dlist2 = []
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i == j:
                dlist1.append(arr[i][j])
            if j == end:
                dlist2.append(arr[i][j])
        end -= 1
    return abs(sum(dlist1) - sum(dlist2))