def gridSearch(G, P):
    """
    G : the grid to search, an array of strings
    P : the pattern to search for, an array of strings
    
    First, check if the first line of pattern P fits into grid G.
    If it does, then check consecutive lines. If the next line also fits into the grid, add 1 to check, if not, set to 0.
    When check is equal to length of P - 1, return "YES"
    """
    check = 0
    for i in range(len(G[0]) - len(P[0]) +1):
        for j in range(len(G) - len(P)+1):
            if G[j][i:i+len(P[0])] == P[0]:
                for k in range(1, len(P)):
                    if G[j+k][i:i+len(P[0])] == P[k]:
                        check +=1
                        if check == len(P)-1:
                            return "YES"
                    else:
                        check = 0
    return "NO"
