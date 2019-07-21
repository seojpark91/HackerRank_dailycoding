def gridChallenge(grid):
    """
    return a string, either YES or NO if rearranging elements of each row alphabetically ascending also results in the columns being in ascending alphabetical order
    
    grid: an array of strings
    """
    
    res = []
    for row in grid:
        res.append(sorted(list(row)))
    
    n_columns = len(res[0])
    
    for i in range(n_columns):
        column = [row[i] for row in res]
        
        if sorted(column) != column:
            return "NO"
    return "YES"