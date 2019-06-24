def happyLadybugs(b):
    """
    b : an array of strings that represents the initial positions and colors of the ladybugs
    
    To make the ladybugs happy there should be at least one empty cell AND no single letter
    OR there is no empty cell but the given string is already happy
    """
    n = len(b)
    
    for a in set(b):
        if a != "_" and b.count(a) == 1:
            return "NO"
    
    if b.count ("_") == 0:
        for i in range(1, n-1):
            if b[i-1] != b[i] and b[i+1] != b[i]:
                return "NO"
    
    return "YES"