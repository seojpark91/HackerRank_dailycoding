def cavityMap(n, grid):
    """
    Given a square matrix of integer strings, find a value which is not on the border of the matrix
    and each value adjacent to ithas strictly smaller.
    
    n : the number of rows and columns in the map
    grid : an array of strings, each representing a row of the grid
    """
    for i in range(1, n-1):
        for j in range(1, n-1):
            if grid[i][j] > max(grid[i-1][j], grid[i+1][j], grid[i][j-1], grid[i][j+1]):
                grid[i] = grid[i][:j] +'X' + grid[i][j+1:]
    return grid
