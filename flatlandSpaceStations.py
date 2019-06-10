def flatlandSpaceStations(n, c): 
    """
    Compare distances between adjacent space stations and
    get the max distance from a middle city to nearest space station.
    
    n: number of cities
    c: a list of space stations
    """
    c.sort()
    # distance from first city to first station is (c[0] - 0)
    # distance from last city to last station is ((n-1) - c[-1]) 
    maximum = max(c[0], n - c[-1] -1)
    
    # only iterate over space stations
    for i in range(1, m): 
        d = c[i] - c[i-1]
        # the distance between two adjacent stations
        # d//2 : the distance from the middle city to either station
        maximum = max(d//2, maximum)
        
    return maximum