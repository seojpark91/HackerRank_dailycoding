def marcsCakewalk(calorie):
    """
    return a long integer that represents the minimum miles necessary.
    parameter: 
    calorie: an integer array that represents calorie count for each cupcake
    """
    reversed_calorie = sorted(calorie, reverse=True)
    return sum([2**i * c for i, c in enumerate(reversed_calorie)])