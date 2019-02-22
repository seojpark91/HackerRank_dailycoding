def matchingStrings(strings, queries):
    counter = Counter(strings) 
    count_list = []   

    for query in queries:
        if query in counter:
            count = counter[query]
            count_list.append(count)
        else:
            count_list.append(0)
    
    return count_list
    
strings = ["aba", "baba", "aba", "xzxb"]
queries = ["aba", "xzxb", "ab"]
matchingStrings(strings, queries)