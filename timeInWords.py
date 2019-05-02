def timeInWords(h, m):
    time_dict = {1: "one", 2:"two", 3:"three", 4: "four",
                5: "five", 6: "six", 7: "seven", 8: "eight",
                9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
                13: "thirteen", 14: "fourteen", 15: "quarter", 
                16: "sixteen", 17: "seventeen", 18: "eighteen",
                19: "nineteen", 20: "twenty", 21:"twenty one",
                 22: "twenty two", 23: "twenty three", 24:"twenty four",
                 25: "twenty five", 26:"twenty six", 27: "twenty seven",
                 28: "twenty eight", 29:"twenty nine", 30: "half", 40: "fourty", 45: "quarter", 50: "fifty"}
    if m == 1:
        min_str = "minute"
    else:
        min_str = "minutes"
        
    if m == 0:
        connect = " o' clock"
        return time_dict[h] + connect

    elif m >= 1 and m <= 30:
        connect="past"    
        if m == 15 or m == 30:
            return time_dict[m] + " " + connect + " " + time_dict[h]
        return time_dict[m] + " " + min_str + " " + connect + " " + time_dict[h]
    
    else:
        connect = "to"
        if 60-m == 1:
            min_str = "minute"
        if m ==45:
            return time_dict[m] + " " + connect + " " + time_dict[h+1]
            
        return time_dict[60-m] + " " + min_str + " " + connect + " " + time_dict[h+1]

timeInWords(5, 31),timeInWords(7, 40),timeInWords(6, 45)