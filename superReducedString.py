def superReducedString(s):
    """
    return the super reduced string or Empty String if the final string is empty.
    
    parameter:
    s : a string to reduce
    
    samples:
    aaabccddd --> abd
    aa --> Empty String
    baab --> Empty String
    """
    pattern = re.compile(r"(.)\1{1}")
    res = re.sub(pattern, r"", s)
    if res == "":
        return "Empty String"
    else:
        if res == re.sub(pattern, r"", res):
            return res
        else:
            while res != re.sub(pattern, r"", res):
                res = re.sub(pattern, r"", res)
                if res == "":
                    return "Empty String"
            return res
        

if __name__ == '__main__':
    print("aaabccddd --> {}, baab --> {}, aa --> {}".format(superReducedString('aaabccddd'),superReducedString('baab'), superReducedString('aa')))