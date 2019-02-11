def dynamicArray(n, queries):
    seqList = [[] for i in range(0,n)]
    lastAnswer = 0
    result = []
    for q in queries:
        index = (q[1] ^ lastAnswer) % n
        if q[0]==1:
            seqList[index].append(q[2])
        else:
            column = q[2] % len(seqList[index])
            lastAnswer = seqList[index][column]
            result.append(lastAnswer)

    return result