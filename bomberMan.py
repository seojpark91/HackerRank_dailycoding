def bomberMan(n, grid):
    """
    return an array of strings that represent the grid in its final state
    
    parameters:
    n: an integer, the number of seconds to simulate
    grid: an array of strings that represents the grid
    """
    if n in [0,1]: 
        return grid
    elif n % 2 == 0: 
        return ['O' * len(x) for x in grid]
    else:
        # symbols replacement
        grid = [x.replace('O', '2') for x in grid]
        grid = [x.replace('.', '0') for x in grid]
    
        # make a list 
        grid = [list(map(int, list(x))) for x in grid]
        
        time = 1
        rows = len(grid)
        columns = len(grid[0])
        
        while time < 4 + n % 4:
            time += 1
            exploded = []
            
            for row in range(rows):
                for column in range(columns):
                    if grid[row][column] > 0: 
                        grid[row][column] -= 1
                    # plant bombs
                    if time % 2 == 0 and grid[row][column] == 0:
                        grid[row][column] = 3
                        
                    #explosion
                    elif grid[row][column] == 0:
                        exploded.append([row,column])
                        if row < rows - 1:
                            exploded.append([row+1, column])
                        if row > 0:
                            exploded.append([row-1, column])
                        if column < columns -1:
                            exploded.append([row, column+1])
                        if column > 0:
                            exploded.append([row, column-1])
            if exploded:
                # refill bombs
                grid = [[2] * len(x) for x in grid]
                for row, column in exploded:
                    grid[row][column] = 0
        # convert lists to strings
        grid = [''.join(list(map(str, x))) for x in grid]
            
        #replace symbols
        grid = [x.replace('2', 'O') for x in grid]
        grid = [x.replace('0', '.') for x in grid]
            
        return grid