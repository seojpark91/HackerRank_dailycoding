def camelcase(s):
"""
return the integer number of words in the input string

parameter:
s: the string to analyze
"""
    num =0 
    for word in s:
        if word.isupper():
            num +=1
    return num + 1