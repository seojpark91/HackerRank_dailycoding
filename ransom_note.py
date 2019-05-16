from collections import Counter 

def ransom_note(magazine, ransom):
    len_ran = len(ransom.split(" "))
    count = 0
    count_magazine = Counter(magazine.split(" "))
    count_ransom = Counter(ransom.split(" "))
    
    
    for w in count_ransom:
        if count == len_ran:
            break
        elif w in count_magazine and count_ransom[w] == count_magazine[w]:
            count += 1
    if count == len_ran:
        return "Yes"
    
    return "No"

ransom_note('two times three is not four', 'two times two is four'), ransom_note('ive got a lovely bunch of coconuts','ive got some coconuts'), ransom_note('give me one grand today night','give one grand today')
