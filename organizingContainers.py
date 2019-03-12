def organizingContainers(container):
    row_sum = []
    for i, r in enumerate(container):
        row_sum.append(sum(r))
        
    col_sum = [sum(i) for i in list(zip(*container))]
    row_sum.sort() # make sure both lists contain same elements in equal numbers
    col_sum.sort()
    
    if col_sum == row_sum:
        return 'Possible'
    else:
        return 'Impossible'

organizingContainers([[1,1],[1,1]]), organizingContainers([[1,3,1],[2,1,2],[3,3,3]])

