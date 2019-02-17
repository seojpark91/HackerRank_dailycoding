def permutationEquation(p):
    num = {n:i for i, n in enumerate(p,1)}
    result = []
    for i in range(1, len(p)+1):
        result.append(num[num[i]])
    return result