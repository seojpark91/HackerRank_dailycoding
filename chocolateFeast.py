def chocolateFeast(n, c, m):
    # initialize the number of chocolates, wrappers, eat (how many chocolates one ate)
    chocolates = wrappers = n//c
    eat = chocolates

    while m <= wrappers: # if there are enough wrappers to exchange 
        chocolates = wrappers // m # one can eat more chocolates
        eat += chocolates
        wrappers = (wrappers % m) + chocolates # add wrappers
    return eat