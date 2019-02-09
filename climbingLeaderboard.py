def climbingLeaderboard(scores, alice):
# in order to reduce time complexity, we only iterate once
# I could have also used sorted(set(scores), reverse = True). but, this iterates over the list twice
    result = []
    ranking = [scores[0]]
    for score in scores:
        if score != ranking[-1]:
            ranking.append(score)
     
    idx = len(ranking) -1 
    
    for score in alice:
# loop through until alice's score is equal to or becomes less than a score on the ranking board
        while idx >= 0 and ranking[idx] < score: 
            idx -= 1
        
        if ranking[idx] == score:
            result.append(idx +1)
        else:
            result.append(idx +2)
    
    return result