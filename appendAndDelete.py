def appendAndDelete(s, t, k):
    s_length = len(s)
    t_length = len(t)
    
    if s_length + t_length < k:
        return "Yes"
    
    same = 0
    for letter_s, letter_t, in zip(s,t):
        if letter_s == letter_t:
            same +=1
        else:
            break
    
    extra_s = s_length - same
    extra_t = t_length - same
    difference = extra_s + extra_t
    
    if difference <= k and difference%2 == k%2:
        return "Yes"
    return "No"

appendAndDelete('zzzzz', 'zzzzzzz',4, appendAndDelete('ashley', 'ash', 2), appendAndDelete('abc', 'def', 6), appendAndDelete('hackerhappy','hackerrank', 9)