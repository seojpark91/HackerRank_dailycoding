def circularArrayRotation(a, k, queries):
    result = []
    while k:
        a.insert(0, a.pop(-1))
        k -=1
    
    for q in queries:
        result.append(a[q])
    return result

circularArrayRotation([3,4,5], 2, [1,2])