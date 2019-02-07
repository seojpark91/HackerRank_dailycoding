from itertools import accumulate

def arrayManipulation(n, queries):
    result = [0 for _ in range(n+1)]
    for a, b, k in queries:
        result[a-1] += k
        result[b] += -k
    
    return max(accumulate(result))

test = [[1, 2, 100],[2, 5, 100],[3, 4, 100]]
arrayManipulation(5,test)

