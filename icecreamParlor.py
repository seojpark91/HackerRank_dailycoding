def icecreamParlor(m, arr):   
    """
    problem : given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have
    
    parameters:
    m: an integer denoting the amount of money they have to spend
    arr: an integer array denoting the cost of each flavor of ice cream
    
    return:
    an array containing the indices of the prices of the two flavors they buy, sorted ascending
    """
    index_dict = {i+1:num for i, num in enumerate(arr)}
    counter = Counter(arr)
    res = []
    
    for index, value in index_dict.items():
        if (m - value > 0) and (m - value in arr):
            if value == m-value:
                if counter[value] == 2:
                    res.append(index)
            else:
                res.append(index)
    return res