def bigSorting(unsorted):
    """
    unsorted : unsorted list of integers in string format
    This problem at first looked easy, but for the first attempt, I failed 9 out of 4 cases due to runout error
    The reason behind this runout error was string --> int, and int --> string data type conversion.
    I found the sorted function has 'key' parameter which one can pass data type to sort, but it does not change the actual list.
    This passed the whole test cases. 
    """
    return [i for i in sorted(unsorted, key=int)]
