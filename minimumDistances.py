def minimumDistances(a):
    temp = {}
    ls = []
    for i, num in enumerate(a):
        if not temp.get(num):
            temp[num] = [i]
        else:
            temp[num].append(i)
    
        if len(temp[num]) == 2:
            ls.append(temp[num][1] - temp[num][0])
    
    if not ls:
        return -1
    else:
        return min(ls)

minimumDistances([7, 1, 3, 4, 1, 7]), minimumDistances([1, 2, 3, 4, 10])