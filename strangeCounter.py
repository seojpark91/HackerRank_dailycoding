def strangeCounter(t):
    """
    t : a single integer denoting the value of time t
    
    the last value of one cycle has the general form of 3 * (2**k - 1)
    the first cycle has the last value of 3, which is 3 * (2 ** 1 -1) = 3 * 1
    the second cycle has the last value of 9, which is 3 * (2 ** 2 -1) = 3 * 3 
    
    Therefore with while loop, we increment the value k until the last value becomes less than query value t
    The relationship between the last value and the query value t is last value - query value + 1
    """
    k = 1
    while t > 3 * (2**k - 1):
        k += 1
    last_value = 3 * (2**k - 1)
    return last_value - t + 1

if __name__ == '__main__':
    print("with t = 4 --> {}, with t = 17 --> {}".format(strangeCounter(4), strangeCounter(17)))