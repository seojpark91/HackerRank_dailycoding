from collections import Counter

def migratoryBirds(arr):
    arr = sorted(arr)
    counter = Counter(arr)
    return counter.most_common()[0][0]    