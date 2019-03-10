from collections import Counter
from itertools import combinations


# First, I thought the only way to solve this problem was brute force. I only got 4/9 of the test codes
def acmTeam(topic):
    members = list(combinations(list(range(1, n+1)), 2))
    final = []

    for mem in members:
        count = 0
        for j in range(m):
            if topic[mem[0]-1][j] or topic[mem[1]-1][j] == 1:
                count +=1
        final.append(count)
    max_n = max(final)
    counter = Counter(final)
    return [max_n, counter[max_n]]


# Then, after reading the comments, I realized that there is no need to get all the combinations of the given topic
def acmTeam(topics):
    comb_topics = combinations(topics,2)
    max_topics = 0
    count = 0
    for topic in comb_topics:
        # turn the topic string into bits to do bitwise operation OR on two sets and count the number of '1's
        num = str(bin(((int(topic[0],2) | int(topic[1],2)))))[2:].count('1') 
        if num > max_topics:            
            max_topics = num
            count = 1
        elif num == max_topics:
            count += 1
    return (max_topics, count)