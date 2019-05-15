def number_needed(a, b):
    count = 0
    # get frequencies and unique letters from each string
    counter_a = Counter(a)
    counter_b = Counter(b)
    
    for n in counter_a:
        if n in counter_b:
    # if two strings include selected letter but have different frequencies, add the absolute value of the difference
            if counter_a[n] != counter_b[n]:
                count += abs(counter_a[n] - counter_b[n])
        else: # if n not in string b add the frequency of selected letter
            count += counter_a[n]
    
    for n in counter_b: 
        if n not in counter_a: # if n not in string a add the frequency of selected letter
            count += counter_b[n]
        
    return count

number_needed('bacdc', 'dcbad'), number_needed('cde', 'abc'), number_needed('bacdc', 'dcbac')