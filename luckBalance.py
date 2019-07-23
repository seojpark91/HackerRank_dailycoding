def luckBalance(k, contests):
    """
    return an integer that represents the maximum luck balance achievable
    
    parameters:
    k: the number of important contests Lena can lose
    contests: a 2D array of integers where each contests[i] contains two integers that represent the luck balance and importance of the ith contest
    """
    num_important = 0
    important_contests = []
    unimportant_contests = []
    
    for contest in contests:
        if contest[1] == 1:
            num_important += 1
            important_contests.append(contest[0])
        else:
            unimportant_contests.append(contest[0])
            
    sorted_important_contests = sorted(important_contests)
    total_contests = sorted_important_contests + unimportant_contests
    
    if k < num_important:
        return sum(total_contests[num_important - k:]) - sum(total_contests[:num_important - k]) 
    else:
        return sum(total_contests)