from math import floor, ceil, sqrt

def encryption(s):
    new_s = s.replace(" ", "")
    s_len = len(new_s)
    idx = 0
    
    row = floor(sqrt(s_len))
    col = ceil(sqrt(s_len))
    
    if row * col < s_len:
        row += 1
    temp = []
    for r in range(1, row+1):
        temp.append(new_s[idx:idx+col])
        idx += col

    final=[]
    for c in range(0, col):
        for word in temp:
            if c < len(word):
                final.append(word[c])
            else:
                final.append("")
        final.append(" ")
    
    return str.rstrip("".join(final))

encryption('chillout'), encryption('haveaniceday')