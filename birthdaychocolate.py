def birthday(s, d, m):

    count = 0
    
    for i,_ in enumerate(s):
        total = sum(s[i:i+m])
        if total == d:
            count+=1

                
    return count