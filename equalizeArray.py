from collections import Counter

def equalizeArray(arr):
    counter = Counter(arr)
    return len(arr) - counter.most_common(1)[0][1]

equalizeArray([3, 3, 2, 1, 3]), equalizeArray([1, 2, 3, 1, 2, 3, 3, 3])